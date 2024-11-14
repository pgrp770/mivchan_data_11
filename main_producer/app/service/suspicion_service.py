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