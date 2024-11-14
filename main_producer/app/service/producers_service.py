def organize_list_by_order_of_priority(li, word):
    return sorted(li, key=lambda sentence: word in sentence, reverse=True)


def organize_messages_list(message, word):
    message["sentences"] = organize_list_by_order_of_priority(message["sentences"], word)


if __name__ == '__main__':
    a = {"df": "a", "sentences": ["a", "b"]}
    organize_messages_list(a, "b")
    print(a)
