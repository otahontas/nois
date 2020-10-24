from ariadne import QueryType, MutationType
import datetime
import logging

query = QueryType()
mutation = MutationType()

messages = [
    {
        "id": "1",
        "title": "Eka",
        "recordingUrl": "https://jees.com/eka",
        "createdAt": "2017-01-01T00:00:00",
    },
    {
        "id": "2",
        "title": "Toka",
        "recordingUrl": "https://jees.com/toka",
        "createdAt": "2017-02-01T00:00:00",
    },
]


@query.field("message")
async def resolve_message(*args, id):
    return next(message for message in messages if message["id"] == id)


@query.field("allMessages")
async def resolve_all_messages(*args):
    return messages


@mutation.field("createMessage")
async def resolve_create_message(_, info, message):
    new_message = {
        "id": str(len(messages) + 1),
        "title": message["title"],
        "recordingUrl": "https://jees.com/uusi",
        "createdAt": "2017-01-01T00:00:00"
    }
    messages.append(new_message)
    return new_message
