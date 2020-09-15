from graphene import ObjectType, String, List, ID


class Thread(ObjectType):
    id = ID(required=True)
    messages = List(lambda: Message)


class Message(ObjectType):
    id = ID(required=True)
    content_filename = String(required=True)
