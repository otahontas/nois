from graphene import ObjectType, Field

from .types.message import Message
from .types.thread import Thread

class Query(ObjectType):
    message = Field(Message)
    thread = Field(Thread)

