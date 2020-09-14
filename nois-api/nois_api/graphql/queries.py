from graphene import ObjectType, Field

from .types import Message
from .types import Thread

class Query(ObjectType):
    message = Field(Message)
    thread = Field(Thread)

