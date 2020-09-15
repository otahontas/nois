from . import db


class ThreadModel(db.Model):
    __tablename__ = "threads"

    id = db.Column(db.Integer(), primary_key=True)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._messages = set()

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def add_message(self, message):
        self._messages.add(message)


class MessageModel(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer(), primary_key=True)
    content_url = db.Column(db.String(), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey("threads.id"), nullable=False)
