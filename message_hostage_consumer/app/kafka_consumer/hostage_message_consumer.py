from dotenv import load_dotenv

import os

from kafka_sttings.consumer import consume
from message_hostage_consumer.app.service.consumer_service import insert_message_to_postgres_hostages

load_dotenv(verbose=True)
hostage_messages_topic = os.environ['HOSTAGE_MESSAGES_TOPIC']


def consume_message_hostage():
    print("consume message to hostage message")
    consume(
        topic=hostage_messages_topic,
        function=insert_message_to_postgres_hostages
    )
