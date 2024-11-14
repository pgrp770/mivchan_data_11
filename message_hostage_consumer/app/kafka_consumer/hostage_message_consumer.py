from dotenv import load_dotenv

import os

from kafka_sttings.consumer import consume
from message_all_consumer.app.repository.message_repository import create_message

load_dotenv(verbose=True)
hostage_messages_topic = os.environ['HOSTAGE_MESSAGES_TOPIC']


def consume_message_hostage():
    print("consume message to all messages")
    consume(
        topic=hostage_messages_topic,
        function=print
    )
