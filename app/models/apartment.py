from .. import db

class Apartment(db.Model):
    __tablename__ = 'apartments'
    apartment_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    available_from = db.Column(db.Date, nullable=False)
    available_until = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    number_of_rooms = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    price_per_month = db.Column(db.Float, nullable=False)
    
    def serialize(self):
        return {
            'apartment_id': self.apartment_id,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'description': self.description,
            'available_from': self.available_from.isoformat(),
            'available_until': self.available_until.isoformat(),
            'created_at': self.created_at.isoformat(),
            'number_of_rooms': self.number_of_rooms,
            'owner_id': self.owner_id,
            'price_per_month': self.price_per_month
        }

