from .. import db

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class ConversationParticipant(db.Model):
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    joined_at = db.Column(db.DateTime, server_default=db.func.now())
    user = db.relationship('User')

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'))
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    read_at = db.Column(db.DateTime)
    conversation = db.relationship('Conversation', backref=db.backref('messages', lazy=True))
    sender = db.relationship('User')
