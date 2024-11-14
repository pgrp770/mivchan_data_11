from dotenv import load_dotenv

import os

from kafka_sttings.producer import produce

load_dotenv(verbose=True)
hostage_messages_topic = os.environ['HOSTAGE_MESSAGES_TOPIC']


def produce_hostage_messages(message):

    produce(
        topic=hostage_messages_topic,
        key=message['id'],
        value=message
    )
    print(f"produce hostage message {message['id']}{message['sentences']}")
