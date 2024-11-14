from dotenv import load_dotenv

import os

from kafka_sttings.producer import produce

load_dotenv(verbose=True)
all_messages_topic = os.environ['ALL_MESSAGES_TOPIC']


def produce_all_messages(message):
    produce(
        topic=all_messages_topic,
        key=message['id'],
        value=message)
