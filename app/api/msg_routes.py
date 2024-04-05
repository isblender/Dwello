from flask import Blueprint, jsonify, session, request
from ..models.conversation import Conversation, ConversationParticipant, Message
from ..models.user import User
from .. import db

msg_blueprint = Blueprint('msg', __name__)

@msg_blueprint.route('/all', methods=['POST'])
def get_user_conversations():
    data = request.get_json()
    user_id = data.get('user_id')

    user_conversations = (db.session.query(Conversation, Message, User.username)
                          .join(ConversationParticipant)
                          .join(Message)
                          .join(User, User.id == ConversationParticipant.user_id)
                          .filter(ConversationParticipant.user_id == user_id)
                          .order_by(Message.created_at.desc())  # Order by message creation date in descending order
                          .all())

    conversations_data = []
    for conversation, message, username in user_conversations:
        conversation_data = {
            'conversation_id': conversation.id,
            'created_at': conversation.created_at,
            'other_user_name': username if message.sender_id != user_id else None,
            'last_message_text': message.message_text if message else None,
            'last_message_created_at': message.created_at if message else None
        }
        conversations_data.append(conversation_data)

    return jsonify(conversations_data), 200

@msg_blueprint.route('/conversation', methods=['POST'])
def get_conversation_messages():
    data = request.get_json()
    user_id = data.get('user_id')
    other_user_id = data.get('other_user_id')

    # Query the conversation ID where both users are participants
    conversation = (db.session.query(ConversationParticipant.conversation_id)
                    .filter(ConversationParticipant.user_id.in_([user_id, other_user_id]))
                    .group_by(ConversationParticipant.conversation_id)
                    .having(db.func.count(ConversationParticipant.conversation_id) == 2)
                    .scalar())

    if conversation:
        # Get the conversation participants' names
        participants_names = (db.session.query(User.username)
                              .join(ConversationParticipant, User.id == ConversationParticipant.user_id)
                              .filter(ConversationParticipant.conversation_id == conversation)
                              .all())
        user_name, other_user_name = [name[0] for name in participants_names]

        # Get all messages in the conversation along with sender's name
        conversation_messages = (db.session.query(Message, User.username)
                                 .join(User, Message.sender_id == User.id)
                                 .filter(and_(Message.conversation_id == conversation,
                                              Message.sender_id.in_([user_id, other_user_id])))
                                 .order_by(Message.created_at)
                                 .all())

        messages_data = [{
            'sender_name': sender_name,
            'message_text': message.message_text,
            'created_at': message.created_at
        } for message, sender_name in conversation_messages]

        return jsonify({'user_name': user_name, 'other_user_name': other_user_name, 'messages': messages_data}), 200
    else:
        return jsonify({'error': 'Conversation not found'}), 404