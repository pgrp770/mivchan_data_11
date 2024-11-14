from flask import Blueprint, request, jsonify

from main_producer.app.kafka_producer.all_message_producer import produce_all_messages
from main_producer.app.kafka_producer.explosive_message_producer import produce_explosive_messages
from main_producer.app.kafka_producer.hostage_message_producer import produce_hostage_messages
from main_producer.app.service.producers_service import organize_messages_list

message_blueprint = Blueprint('message_bluprint', __name__)


@message_blueprint.route('/', methods=['POST'])
def post_message():
    message = request.json
    produce_all_messages(message)
    if any("explos" in sentence for sentence in message["sentences"]):
        organize_messages_list(message, "explos")
        produce_explosive_messages(message)
    elif any("hostage" in sentence for sentence in message["sentences"]):
        organize_messages_list(message, "hostage")
        produce_hostage_messages(message)
    return jsonify("i have got your messages"), 200
