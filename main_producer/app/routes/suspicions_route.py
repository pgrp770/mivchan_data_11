from flask import Blueprint, jsonify

from main_producer.app.service.suspicion_service import get_list_of_all_sentences, find_most_common_word

suspicions_blueprint = Blueprint('suspicions_bluprint', __name__)


@suspicions_blueprint.route('/sentences_by_email/<string:email>', methods=['GET'])
def get_suspicions_message_by_email(email):
    sentences = get_list_of_all_sentences(email)
    return jsonify({"sentences": sentences}), 200


@suspicions_blueprint.route('/most_common_word', methods=['GET'])
def get_most_common_word():
    sentences = find_most_common_word()
    return jsonify({"most_common_word": sentences}), 200
