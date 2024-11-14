from db.postgress_db.database import session_maker
from db.postgress_db.models import *


def get_sentences_hostage_by_email(email):
    with session_maker() as session:
        sentences = (session.query(SuspiciousHostageContent)
                     .join(User)
                     .filter(User.email == email)
                     .all())

        return sentences


def get_sentences_explosive_by_email(email):
    with session_maker() as session:
        sentences = (session.query(SuspiciousExplosiveContent)
                     .join(User)
                     .filter(User.email == email)
                     .all())

        return sentences


