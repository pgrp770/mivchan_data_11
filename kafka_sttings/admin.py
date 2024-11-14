import os
from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

load_dotenv(verbose=True)


def init_topics():
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    message_all = NewTopic(
        name=os.environ['ALL_MESSAGES_TOPIC'],
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
    )
    message_explosive = NewTopic(
        name=os.environ['EXPLOSIVE_MESSAGES_TOPIC'],
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
    )
    message_hostage = NewTopic(
        name=os.environ['HOSTAGE_MESSAGES_TOPIC'],
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
    )
    try:
        client.create_topics([message_all, message_explosive, message_hostage])
    except TopicAlreadyExistsError as e:
        print(e)
    finally:
        client.close()


if __name__ == '__main__':
    init_topics()
