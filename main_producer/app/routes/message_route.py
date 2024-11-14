from flask import Blueprint, request, jsonify

message_blueprint = Blueprint('message_bluprint', __name__)


@message_blueprint.route('/', methods=['POST'])
def new_member():
    member = request.json
    # for sentence in member["sentences"]:
    #     if "explosive"
    return jsonify("i have got your messages"), 200
