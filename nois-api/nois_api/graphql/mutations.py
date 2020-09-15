from graphene import ObjectType, Mutation, String, Boolean, Field, Int
from .types import Message, Thread
from ..gino.models import MessageModel, ThreadModel

from pprint import pprint


class CreateMessage(Mutation):
    class Arguments:
        content_filename = String(required=True)
        thread_id = String(required=True)

    message = Field(Message)

    async def mutate(root, info, content_filename, thread_id):
        message = await MessageModel.create(
            content_filename=content_filename, thread_id=thread_id
        )
        return CreateMessage(message=message)


class CreateThread(Mutation):
    thread = Field(Thread)

    async def mutate(root, info):
        thread = await ThreadModel.create()
        return CreateThread(thread=thread)


class Mutation(ObjectType):
    create_message = CreateMessage.Field()
    create_thread = CreateThread.Field()
