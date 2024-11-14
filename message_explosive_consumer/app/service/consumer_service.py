from toolz import pipe
from toolz.curried import partial

from db.postgress_db.models import *
from message_explosive_consumer.app.repository.insertion_repository import create_user, create_location, \
    create_device_info, create_explosive_sentences





def message_to_device_info(message, user_id) -> DeviceInfo:
    new_device = message["device_info"]
    device_to_insert: DeviceInfo = DeviceInfo(
        user_id=user_id,
        browser=new_device["browser"],
        os=new_device["os"],
        device_id=new_device["device_id"]
    )
    return device_to_insert


def message_to_location(message, user_id) -> Location:
    new_location = message["location"]
    location_to_insert: Location = Location(
        user_id=user_id,
        latitude=new_location["latitude"],
        longitude=new_location["longitude"],
        city=new_location["city"],
        country=new_location["country"]
    )
    return location_to_insert


def message_to_user(message):
    new_user = User(
        email=message["email"],
        username=message["username"],
        ip_address=message["ip_address"],
        created_at=message["created_at"]
    )
    return new_user


def message_to_sentence(message, user_id, type_sentence=None):
    return pipe(
        message["sentences"],
        partial(map, lambda sentence: SuspiciousExplosiveContent(
            user_id=user_id,
            sentence=sentence
        )),
        list
    )


def insert_message_to_postgres(message):
    new_user = create_user(message_to_user(message))

    create_location(message_to_location(message, new_user.id))
    create_device_info(message_to_device_info(message, new_user.id))

    create_explosive_sentences(message_to_sentence(message, new_user.id))

if __name__ == '__main__':
    aba = {
        "email": "jeremy37@example.org",
        "username": "jonesalejandra",
        "ip_address": "215.67.111.124",
        "created_at": "2024-10-15T05:29:13.450066",
        "location": {
            "latitude": 8.5478895,
            "longitude": -135.24204,
            "city": "Port Josephburgh",
            "country": "PA"
        },
        "device_info": {
            "browser": "Mozilla/5.0",
            "os": "iOS",
            "device_id": "c4a3ce0d-4f4f-4bc9-9e94-b135e32cfe81"
        },
        "sentences": [
            "Public quickly spend hear sing.",
            "Difference nothing environmental shake decide.",
            "Natural southern what nice."
        ]
    }

    insert_message_to_postgres(aba)