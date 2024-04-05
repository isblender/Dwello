from .. import db

class Apartment(db.Model):
    __tablename__ = 'apartments'
    apartment_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    school = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    available_from = db.Column(db.Date, nullable=False)
    available_until = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    price_per_month = db.Column(db.Float, nullable=False)
    looking_for_gender = db.Column(db.String(10), nullable=False)
    looking_for_number = db.Column(db.Integer, nullable=False)
    def serialize(self):
        return {
            'apartment_id': self.apartment_id,
            'address': self.address,
            'description': self.description,
            'available_from': self.available_from,
            'available_until': self.available_until,
            'created_at': self.created_at,
            'looking_for_gender': self.looking_for_gender,
            'looking_for_number': self.looking_for_number,
            'owner_id': self.owner_id,
            'price_per_month': self.price_per_month
        }

