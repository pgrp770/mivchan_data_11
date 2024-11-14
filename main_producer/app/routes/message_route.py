from flask import Blueprint, request, jsonify

from main_producer.app.service.producers_service import filter_messages_to_consumers

message_blueprint = Blueprint('message_bluprint', __name__)


@message_blueprint.route('/', methods=['POST'])
def post_message():
    message = request.json
    filter_messages_to_consumers(message)
    return jsonify("i have got your messages"), 200
