from graphene import ObjectType, String, List, ID


class Thread(ObjectType):
    id = ID(required=True)
    messages = List(lambda: Message)


class Message(ObjectType):
    id = ID(required=True)
    content_location = String(required=True)

    def resolve_content_location(parent, info):
        return info.context["request"].url_for(
            "files:stream_file", filename=parent.content_filename
        )
