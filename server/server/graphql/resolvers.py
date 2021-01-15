from ariadne import QueryType, MutationType
from datetime import datetime, timezone
from server.database import db
from server.database.utils import turn_dict_to_edgeql_expression
from server.file_io import save_file
from mimetypes import guess_extension
import json

query = QueryType()
mutation = MutationType()


def parse_message(data, request):
    _id = data["id"]
    file_extension = data["recording_extension"]
    filename = f"{_id}.{file_extension}"
    url = request.url_for("api:get_file", filename=filename)
    print(url)
    recording_url = f"http://localhost:8000/api/files/{filename}"
    return {**data, "recording_url": recording_url}


@query.field("getMessage")
async def resolve_message(_, info, id):
    """Return message metadata."""
    pool = await db.get_pool()
    async with pool.acquire() as con:
        result = await con.query_one_json(
            """SELECT Message {
                id,
                title,
                created_at,
                recording_content_type,
                recording_extension
                }
                FILTER .id = <uuid>$id""",
            id=id,
        )
    return parse_message(json.loads(result), info.context["request"])


@query.field("getMessages")
async def resolve_all_messages(_, info):
    """Return message metadata for all messages."""
    pool = await db.get_pool()
    async with pool.acquire() as con:
        result = await con.query_one_json(
            """SELECT <json>(
                data := array_agg((
                    SELECT Message {
                        id,
                        title,
                        created_at,
                        recording_content_type,
                        recording_extension
                    }
                ))
            )"""
        )
    result_json = json.loads(result)
    messages = []
    for message in result_json["data"]:
        messages.append(parse_message(message, info.context["request"]))
    return messages


@mutation.field("createMessage")
async def resolve_create_message(_, info, message):
    """Save message metadata to db and recording upload to disk."""
    try:
        file_extension = message["recording"].filename.split(".")[-1]
    except IndexError:
        file_extension = guess_extension(message["content_type"])

    message_to_db = {
        "title": message["title"],
        "created_at": datetime.now(timezone.utc),
        "recording_content_type": message["recording"].content_type,
        "recording_extension": file_extension,
    }

    edgeql_expression = turn_dict_to_edgeql_expression(message_to_db)
    pool = await db.get_pool()
    async with pool.acquire() as con:
        result = await con.query_one_json(
            f"""SELECT (
                    INSERT Message {{
                        {edgeql_expression}
                    }}
                ) {{
                    id,
                    title,
                    created_at,
                    recording_content_type,
                    recording_extension
                }}""",
            **message_to_db,
        )
    message_to_return = parse_message(json.loads(result), info.context["request"])
    _id = result["id"]
    file_extension = result["recording_extension"]
    filename = f"{_id}.{file_extension}"
    await save_file(filename, message["recording"])
    return message_to_return
