from main_producer.app.kafka_producer.all_message_producer import produce_all_messages
from main_producer.app.kafka_producer.explosive_message_producer import produce_explosive_messages
from main_producer.app.kafka_producer.hostage_message_producer import produce_hostage_messages


def organize_list_by_order_of_priority(li, word):
    return sorted(li, key=lambda sentence: word in sentence, reverse=True)


def organize_messages_list(message, word):
    message["sentences"] = organize_list_by_order_of_priority(message["sentences"], word)


def filter_messages_to_consumers(message):
    produce_all_messages(message)
    if any("explos" in sentence for sentence in message["sentences"]):
        organize_messages_list(message, "explos")
        produce_explosive_messages(message)
    elif any("hostage" in sentence for sentence in message["sentences"]):
        organize_messages_list(message, "hostage")
        produce_hostage_messages(message)
