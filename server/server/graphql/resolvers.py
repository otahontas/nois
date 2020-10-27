from ariadne import QueryType, MutationType
from datetime import datetime, timezone
from server.database import db
from server.database.utils import turn_dict_to_edgeql_expression
from server.file_io import save_file
import json

query = QueryType()
mutation = MutationType()


@query.field("message")
async def resolve_message(*args, _id):
    """Return message metadata."""
    pass


@query.field("allMessages")
async def resolve_all_messages(*args):
    """Return message metadata for all messages."""
    pass


@mutation.field("createMessage")
async def resolve_create_message(_, info, message):
    """Save message metadata to db and recording upload to disk."""
    message_to_db = {
        "title": message["title"],
        "created_at": datetime.now(timezone.utc),
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
                    created_at
                }}""",
            **message_to_db,
        )
    result_json = json.loads(result)
    _id = result_json["id"]
    await save_file(_id, message["recording"])
    recording_url = f"http://localhost/api/files/{_id}"
    return {**result_json, "recordingUrl": recording_url}
