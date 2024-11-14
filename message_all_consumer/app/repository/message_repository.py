from db.mongo_db.database import all_messages_collection


def create_message(message):
    new_message = all_messages_collection.insert_one(message.value)
    return new_message.inserted_id
