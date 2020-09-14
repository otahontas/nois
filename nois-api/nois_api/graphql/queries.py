from graphene import ObjectType, Field, Int, List

from .types import Message
from .types import Thread

from ..gino.models import MessageModel


class Query(ObjectType):
    message = Field(Message, id=Int(required=True))
    messages = List(Message)

    async def resolve_message(root, info, id):
        return await MessageModel.get(id)

    async def resolve_messages(root, info):
        return await MessageModel.query.gino.all()
