from . import db


class ThreadModel(db.Model):
    __tablename__ = "threads"

    id = db.Column(db.Integer(), primary_key=True)


class MessageModel(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer(), primary_key=True)
    content_url = db.Column(db.String(), nullable=False)
