from dotenv import load_dotenv

import os

from kafka_sttings.consumer import consume
from message_all_consumer.app.repository.message_repository import create_message

load_dotenv(verbose=True)
explosive_messages_topic = os.environ['EXPLOSIVE_MESSAGES_TOPIC']


def consume_message_explosive():
    print("consume message to all messages")
    consume(
        topic=explosive_messages_topic,
        function=print
    )
