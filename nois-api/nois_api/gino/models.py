from gino import Gino

db = Gino()

class Thread(db.Model):
    __tablename__ = 'threads'

    id = db.Column(db.Integer(), primary_key=True)

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer(), primary_key=True)
    content_url = db.Column(db.String(), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('threads.id'))
