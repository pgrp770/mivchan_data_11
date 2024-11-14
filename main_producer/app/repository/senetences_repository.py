from sqlalchemy.exc import SQLAlchemyError

from db.postgress_db.database import session_maker
from db.postgress_db.models import *


def get_sentences_hostage_by_email(email):
    with session_maker() as session:
        try:
            sentences = (session.query(SuspiciousHostageContent)
                         .join(User)
                         .filter(User.email == email)
                         .all())

            return sentences
        except SQLAlchemyError as ex:
            print(ex)


def get_sentences_explosive_by_email(email):
    with session_maker() as session:
        try:
            sentences = (session.query(SuspiciousExplosiveContent)
                         .join(User)
                         .filter(User.email == email)
                         .all())

            return sentences
        except SQLAlchemyError as ex:
            print(ex)


def get_all_sentences_explosive():
    with session_maker() as session:
        try:
            return session.query(SuspiciousExplosiveContent).all()
        except SQLAlchemyError as ex:
            print(ex)


def get_all_sentences_hostage():
    with session_maker() as session:
        try:
            return session.query(SuspiciousHostageContent).all()
        except SQLAlchemyError as ex:
            print(ex)
