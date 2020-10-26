from ariadne import QueryType, MutationType
from nois_api.database import get_connection, get_pool
from typing import Dict, Any
from uuid import UUID
from datetime import datetime
from edgedb import NoDataError

query = QueryType()
mutation = MutationType()


def get_type(value: Any) -> str:
    if type(value) == bool:
        return "<bool>"
    elif type(value) == str:
        return "<str>"
    elif type(value) == int:
        return "<int64>"
    elif type(value) == UUID:
        return "<uuid>"
    else:
        raise ValueError("Type not found.")


def get_shape(data: Dict[str, Any]) -> str:
    shape_list = [f"{k} := {get_type(v)}${k}" for k, v in data.items()]
    shape_expr = ", ".join(shape_list)
    return shape_expr


def parse_raw(data):
    return {
        **data,
        "recordingUrl": f"http://localhost/{str(data.id)}"
    }


@query.field("message")
async def resolve_message(*args, id):
    pool = await get_pool()
    print(pool)
    try:
        con = await pool.acquire()
        result = await con.query_one_json(
            """SELECT Message {
                id,
                title,
                created_at
            }
            FILTER .id = <uuid>$id""",
            id=id,
        )
    except NoDataError:
        return None
    item = parse_raw(result)
    return item


@query.field("allMessages")
async def resolve_all_messages(*args):
    pass


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
                        created_at:= <datetime>${datetime.now()}
                        )
                    }}
                ) {{
                    id,
                    title,
                    created_at
                }}""",
            **message,
        )
    finally:
        await pool.release(con)
    item = parse_raw(result)
    return item

