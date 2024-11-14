from dotenv import load_dotenv

import os

from kafka_sttings.producer import produce

load_dotenv(verbose=True)
explosive_messages_topic = os.environ['EXPLOSIVE_MESSAGES_TOPIC']


def produce_explosive_messages(message):
    produce(
        topic=explosive_messages_topic,
        key=message['id'],
        value=message
    )
    print(f"produce explosive message {message['id']}{message['sentences']}")
