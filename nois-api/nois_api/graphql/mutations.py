from graphene import ObjectType, Mutation, String, Boolean, Field
from .types import Message

class CreateMessage(Mutation):
    class Arguments:
        content_url = String()

    ok = Boolean()
    message = Field(Message)

    def mutate(root, info, content_url):
        message = Message(content_url = content_url, id="1")
        ok = True
        return CreateMessage(message=message, ok=ok)

class Mutation(ObjectType):
    create_message = CreateMessage.Field()
