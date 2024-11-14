from typing import List

from sqlalchemy.exc import SQLAlchemyError

from db.postgress_db.database import session_maker
from db.postgress_db.models import *


def create_device_info(new_device_info: DeviceInfo):
    with session_maker() as session:
        try:
            session.query(DeviceInfo).session.add(new_device_info)
            session.commit()
            session.refresh(new_device_info)
            print(f"created new device_info with {new_device_info.id} id")
            return new_device_info
        except SQLAlchemyError as ex:
            print(ex)


def create_location(new_location: Location):
    with session_maker() as session:
        try:
            session.query(Location).session.add(new_location)
            session.commit()
            session.refresh(new_location)
            print(f"created new location with {new_location.id} id")
            return new_location
        except SQLAlchemyError as ex:
            print(ex)


def create_explosive_sentences(new_sentences: List[SuspiciousExplosiveContent]):
    with session_maker() as session:
        try:
            session.query(SuspiciousExplosiveContent).session.add_all(new_sentences)
            session.commit()
            print(f"created new explosive sentences")
        except SQLAlchemyError as ex:
            print(ex)


def create_hostage_sentence(new_sentences: List[SuspiciousHostageContent]):
    with session_maker() as session:
        try:
            session.query(SuspiciousHostageContent).session.add_all(new_sentences)
            session.commit()
            print(f"created new hostage sentences")
        except SQLAlchemyError as ex:
            print(ex)


def create_user(new_user: User):
    with session_maker() as session:
        try:
            session.query(DeviceInfo).session.add(new_user)
            session.commit()
            session.refresh(new_user)
            print(f"create new user with {new_user.id} id")
            return new_user
        except SQLAlchemyError as ex:
            print(ex)
