from flask import Blueprint, request, jsonify
from .. import db
from ..models.apartment import Apartment

apartment_blueprint = Blueprint('apartment', __name__)

@apartment_blueprint.route('/', methods=['GET'])
def get_apartments():
    apartments = Apartment.query.all()
    return jsonify([apartment.serialize() for apartment in apartments])

@apartment_blueprint.route('/', methods=['POST'])
def create_apartment():
    data = request.json

    # Check if all required fields are present in the request data
    required_fields = ['address', 'city', 'state', 'zip_code', 'description', 'available_from', 'available_until', 'number_of_rooms', 'owner_id', 'price_per_month']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400

    try:
        # Create a new apartment object
        new_apartment = Apartment(
            address=data['address'],
            city=data['city'],
            state=data['state'],
            zip_code=data['zip_code'],
            description=data['description'],
            available_from=data['available_from'],
            available_until=data['available_until'],
            number_of_rooms=data['number_of_rooms'],
            owner_id=data['owner_id'],
            price_per_month=data['price_per_month']
        )

        # Add the new apartment to the database
        db.session.add(new_apartment)
        db.session.commit()

        # Return a meaningful response
        return jsonify({
            'message': 'Apartment created successfully!',
            'apartment_id': new_apartment.apartment_id
        }), 201
    except Exception as e:
        # Handle any exceptions (e.g., database errors)
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

