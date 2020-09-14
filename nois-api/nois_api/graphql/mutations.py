from graphene import ObjectType, Mutation, String, Boolean, Field
from .types import Message
from ..gino.models import MessageModel

class CreateMessage(Mutation):
    class Arguments:
        content_url = String()

    ok = Boolean()
    message = Field(Message)

    async def mutate(root, info, content_url):
        message = await MessageModel.create(content_url=content_url)
        print(message)
        m2 = Message(content_url = content_url, id="1")
        ok = True
        return CreateMessage(message=m2, ok=ok)

class Mutation(ObjectType):
    create_message = CreateMessage.Field()
