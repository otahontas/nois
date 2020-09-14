from graphene import ObjectType, String, List, ID

class Thread(ObjectType):
    id = ID()
    messages = List(lambda: Message)

class Message(ObjectType):
    id = ID(required=True)
    content_url = String(required=True)

    async def resolve_content_url(self, info):
        return "http://example.com"
