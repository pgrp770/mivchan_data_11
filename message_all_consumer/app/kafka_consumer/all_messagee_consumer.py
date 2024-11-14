from dotenv import load_dotenv

import os

from kafka_sttings.consumer import consume
from message_all_consumer.app.repository.message_repository import create_message

load_dotenv(verbose=True)
all_messages_topic = os.environ['ALL_MESSAGES_TOPIC']


def consume_members():
    print("consume message to all messages")
    consume(
        topic=all_messages_topic,
        function=create_message
    )
