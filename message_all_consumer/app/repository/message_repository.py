from db.mongo_db.database import all_messages_collection
from pymongo.errors import PyMongoError


def create_message(message):
    try:
        new_message = all_messages_collection.insert_one(message.value)
        print(f"create_message with {new_message.inserted_id} id")
        return new_message.inserted_id
    except PyMongoError as ex:
        print(ex)
