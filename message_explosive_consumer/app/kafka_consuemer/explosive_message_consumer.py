from dotenv import load_dotenv

import os

from kafka_sttings.consumer import consume
from message_all_consumer.app.repository.message_repository import create_message
from message_explosive_consumer.app.service.consumer_service import insert_message_to_postgres

load_dotenv(verbose=True)
explosive_messages_topic = os.environ['EXPLOSIVE_MESSAGES_TOPIC']


def consume_message_explosive():
    print("consume message to explosive messages")
    consume(
        topic=explosive_messages_topic,
        function=insert_message_to_postgres
    )
