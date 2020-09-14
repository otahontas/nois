from graphene import ObjectType, Field

from .types import Message
from .types import Thread

class Query(ObjectType):
    message = Field(Message)

    async def resolve_message(root, info): 
        return Message(
            id="1001",
            content_url="http://example.com"
        )
