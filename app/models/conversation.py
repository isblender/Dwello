from .. import db

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartments.id'), nullable=False)
    initiator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sent_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    
    def serialize(self):
        return {
            'id': self.id,
            'message': self.message,
            'apartment_id': self.apartment_id,
            'initiator_id': self.initiator_id,
            'recipient_id': self.recipient_id,
            'sent_at': self.sent_at.isoformat()
        }