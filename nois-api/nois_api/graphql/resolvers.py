from ariadne import QueryType

query = QueryType()

m1 = {
    "id": "1234",
    "title": "Jou jou jou",
    "recordingUrl": "http://example.com/jeaah"
}
m2 = {
    "id": "1233",
    "title": "Jea jea jea",
    "recordingUrl": "http://example.com/jouuu"
}

messages = [m1,m2]


@query.field("message")
async def resolve_message(*_, id):
    if id == "1234": 
        return m1
    if id == "1233":
        return m2
    return None


# from graphene import ObjectType, Field, List, String
# from asyncpg.exceptions import UndefinedTableError

# from .types import Message, Thread

# from ..gino.models import MessageModel, ThreadModel


# class Query(ObjectType):
#     message = Field(Message, id=String(required=True))
#     messages = List(Message)
#     thread = Field(Thread, id=String(required=True))
#     threads = List(Thread)

#     async def resolve_message(root, info, id):
#         return await MessageModel.get(id)

#     async def resolve_messages(root, info):
#         return await MessageModel.query.gino.all()

#     async def resolve_thread(root, info, id):
#         return await ThreadModel.get(id)

#     async def resolve_threads(root, info):
#         query = ThreadModel.outerjoin(MessageModel).select()
#         try:
#             return await query.gino.load(
#                 ThreadModel.distinct(ThreadModel.id).load(add_message=MessageModel)
#             ).all()
#         except UndefinedTableError as error:
#             print("error happened ", error)
#             return []


# from graphene import ObjectType, Mutation, String, Field
# from .types import Message, Thread
# from ..gino.models import MessageModel, ThreadModel


# class CreateMessage(Mutation):
#     class Arguments:
#         content_filename = String(required=True)
#         thread_id = String(required=True)

#     message = Field(Message)

#     async def mutate(root, info, content_filename, thread_id):
#         message = await MessageModel.create(
#             content_filename=content_filename, thread_id=thread_id
#         )
#         return CreateMessage(message=message)


# class CreateThread(Mutation):
#     thread = Field(Thread)

#     async def mutate(root, info):
#         thread = await ThreadModel.create()
#         return CreateThread(thread=thread)


# class MessageThreadMutation(ObjectType):
#     create_message = CreateMessage.Field()
#     create_thread = CreateThread.Field()
