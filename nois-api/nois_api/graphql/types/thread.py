from graphene import ObjectType, String, List, ID
from .message import Message

class Thread(ObjectType):
    id = ID()
    messages = List(lambda: Message)
