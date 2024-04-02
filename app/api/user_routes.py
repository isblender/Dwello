from flask import Blueprint, jsonify, session, request
from ..models.user import User
from .. import db

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print(f"data: {data}")
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'message': 'Username already exists.'}), 409

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'message': 'Email already exists.'}), 409

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully.'}), 201

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        # Assuming you are using sessions to manage logins
        session['user_id'] = user.user_id
        return jsonify({'message': 'Logged in successfully.'}), 200

    return jsonify({'message': 'Invalid username or password.'}), 401