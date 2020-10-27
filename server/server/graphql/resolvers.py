from ariadne import QueryType, MutationType
from datetime import datetime, timezone
from server.database import db
from server.database.utils import turn_dict_to_edgeql_expression
from server.file_io import save_file
from mimetypes import guess_extension
import json

query = QueryType()
mutation = MutationType()


@query.field("getMessage")
async def resolve_message(*_, _id):
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
                FILTER .id = <uuid>$_id""",
            _id=_id,
        )
    result_json = json.loads(result)
    file_extension = result_json["recording_extension"]
    filename = f"{_id}.{file_extension}"
    recording_url = f"http://localhost:8000/api/files/{filename}"  # fix correct url
    print(recording_url)
    return {**result_json, "recording_url": recording_url}


@query.field("getMessages")
async def resolve_all_messages(*args):
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
    print(result_json)
    return result_json["data"]


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
    result_json = json.loads(result)
    _id = result_json["id"]
    filename = f"{_id}.{file_extension}"
    await save_file(filename, message["recording"])
    recording_url = f"http://localhost:8000/api/files/{filename}"  # fix correct url
    print(recording_url)
    return {**result_json, "recording_url": recording_url}
