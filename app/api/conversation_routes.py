from flask import Blueprint, request, jsonify
from .. import db
from ..models.conversation import Conversation

conversation_blueprint = Blueprint('conversation', __name__)

@conversation_blueprint.route('/', methods=['GET'])
def get_conversations():
    conversations = Conversation.query.all()
    return jsonify([conversation.serialize() for conversation in conversations])

@conversation_blueprint.route('/', methods=['POST'])
def start_conversation():
    data = request.json
    new_conversation = Conversation(
        message=data['message'],
        apartment_id=data['apartment_id'],
        initiator_id=data['initiator_id'],
        recipient_id=data['recipient_id']
    )
    db.session.add(new_conversation)
    db.session.commit()
    return jsonify({'message': 'Conversation started successfully!'}), 201
