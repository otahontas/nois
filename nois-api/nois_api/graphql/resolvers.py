from ariadne import QueryType, MutationType
from nois_api.database import get_connection, get_pool
from typing import Dict, Any

query = QueryType()
mutation = MutationType()


def get_type(value: Any) -> str:
    if type(value) == bool:
        return "<bool>"
    elif type(value) == str:
        return "<str>"
    elif type(value) == int:
        return "<int64>"
    # elif type(value) == UUID:
    #     return "<uuid>"
    else:
        raise ValueError("Type not found.")


def get_shape(data: Dict[str, Any]) -> str:
    shape_list = [f"{k} := {get_type(v)}${k}" for k, v in data.items()]
    shape_expr = ", ".join(shape_list)
    return shape_expr


messages = [
    {
        "id": "1",
        "title": "Eka",
        "recordingUrl": "https://jees.com/eka",
        "createdAt": "2017-01-01T00:00:00",
    },
    {
        "id": "2",
        "title": "Toka",
        "recordingUrl": "https://jees.com/toka",
        "createdAt": "2017-02-01T00:00:00",
    },
]


@query.field("message")
async def resolve_message(*args, id):
    return next(message for message in messages if message["id"] == id)


@query.field("allMessages")
async def resolve_all_messages(*args):
    return messages


@mutation.field("createMessage")
async def resolve_create_message(_, info, message):
    shape_expr = get_shape(message)
    pool = await get_pool()
    try:
        con = await pool.acquire()
        # TODO: error checking and good reporting with graphql
        result = await con.query_one_json(
            f"""SELECT (
                    INSERT Message {{
                        {shape_expr}
                    }}
                ) {{
                    id,
                    title,
                }}""",
            **message,
        )
        print(result)
    finally:
        await pool.release(con)
    new_message = {
        "id": str(len(messages) + 1),
        "title": message["title"],
        "recordingUrl": "https://jees.com/uusi",
        "createdAt": "2017-01-01T00:00:00",
    }
    messages.append(new_message)
    return new_message
