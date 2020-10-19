from graphene import ObjectType, Field, List, String
from asyncpg.exceptions import UndefinedTableError

from .types import Message, Thread

from ..gino.models import MessageModel, ThreadModel


class Query(ObjectType):
    message = Field(Message, id=String(required=True))
    messages = List(Message)
    thread = Field(Thread, id=String(required=True))
    threads = List(Thread)

    async def resolve_message(root, info, id):
        return await MessageModel.get(id)

    async def resolve_messages(root, info):
        return await MessageModel.query.gino.all()

    async def resolve_thread(root, info, id):
        return await ThreadModel.get(id)

    async def resolve_threads(root, info):
        query = ThreadModel.outerjoin(MessageModel).select()
        try:
            return await query.gino.load(
                ThreadModel.distinct(ThreadModel.id).load(add_message=MessageModel)
            ).all()
        except UndefinedTableError as error:
            print("error happened ", error)
            return []
