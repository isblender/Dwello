from flask import Blueprint, request, jsonify, request, session
from .. import db
from ..models.conversation import Conversation

conversation_blueprint = Blueprint('conversation', __name__)

@conversation_blueprint.route('/', methods=['GET'])
def get_conversations():
    data = request.get_json()
    print(f"data: {data}")
    initiator_id = data.get('initiator_id')
    recipient_id = data.get('recipient_id')
    messages = Conversation.query.filter(
        ((Conversation.initiator_id == initiator_id) & (Conversation.recipient_id == recipient_id)) |
        ((Conversation.sender_id == recipient_id) & (Conversation.recipient_id == initiator_id))
    ).all()
    

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
