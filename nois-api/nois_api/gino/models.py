from . import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class BaseModel(db.Model):
    """Base for other models to inherit."""

    id = db.Column(
        UUID,
        primary_key=True,
        default=uuid4,
        unique=True,
        nullable=False,
    )


class ThreadModel(BaseModel):
    __tablename__ = "threads"

    def __init__(self, **kw):
        super().__init__(**kw)
        self._messages = set()

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def add_message(self, message):
        self._messages.add(message)


class MessageModel(BaseModel):
    __tablename__ = "messages"

    content_filename = db.Column(db.String(), nullable=False)
    thread_id = db.Column(UUID, db.ForeignKey("threads.id"), nullable=False)
