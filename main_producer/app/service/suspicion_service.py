from collections import Counter

from toolz import pipe
from toolz.curried import partial

from main_producer.app.repository.senetences_repository import *


def get_list_of_all_sentences(email):
    sentences_hostage = get_sentences_hostage_by_email(email)
    sentences_explosive = get_sentences_explosive_by_email(email)
    return pipe(
        sentences_hostage + sentences_explosive,
        partial(map, lambda sentence: sentence.sentence),
        list
    )


def find_most_common_word():
    sentences_hostage = get_all_sentences_hostage()
    sentences_explosive = get_all_sentences_explosive()
    all_sentences = pipe(
        sentences_explosive + sentences_hostage,
        partial(map, lambda s: s.sentence),
        list,
        "".join,
        lambda s: s.replace(".", " "),
        lambda s: s.split(),
        lambda li: Counter(li).most_common(),
        lambda li: li[0][0]

    )
    return all_sentences


if __name__ == '__main__':
    print(find_most_common_word())
