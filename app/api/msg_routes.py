from flask import Blueprint, jsonify, session, request
from ..models.conversation import Conversation, ConversationParticipant, Message
from .. import db

msg_blueprint = Blueprint('msg', __name__)