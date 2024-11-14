from flask import Blueprint, request, jsonify

from main_producer.app.kafka_producer.all_message_producer import produce_all_messages
from main_producer.app.kafka_producer.explosive_message_producer import produce_explosive_messages
from main_producer.app.kafka_producer.hostage_message_producer import produce_hostage_messages
from main_producer.app.service.producers_service import organize_messages_list
from main_producer.app.service.suspicion_service import get_list_of_all_sentences

suspicions_blueprint = Blueprint('suspicions_bluprint', __name__)


@suspicions_blueprint.route('/sentences_by_email/<string:email>', methods=['GET'])
def get_suspicions_message_by_email(email):
    sentences = get_list_of_all_sentences(email)
    return jsonify({"sentences": sentences}), 200
