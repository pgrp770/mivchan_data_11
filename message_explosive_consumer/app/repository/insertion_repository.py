from typing import List

from db.postgress_db.database import session_maker
from db.postgress_db.models import *


def create_device_info(new_device_info: DeviceInfo):
    with session_maker() as session:
        session.query(DeviceInfo).session.add(new_device_info)
        session.commit()
        session.refresh(new_device_info)
        return new_device_info


def create_location(new_location: Location):
    with session_maker() as session:
        session.query(Location).session.add(new_location)
        session.commit()
        session.refresh(new_location)
        return new_location


def create_explosive_sentences(new_sentences: List[SuspiciousExplosiveContent]):
    with session_maker() as session:
        session.query(SuspiciousExplosiveContent).session.add_all(new_sentences)
        session.commit()


def create_hostage_sentence(new_sentences: List[SuspiciousHostageContent]):
    with session_maker() as session:
        session.query(SuspiciousHostageContent).session.add(new_sentences)
        session.commit()


def create_user(new_user: User):
    with session_maker() as session:
        session.query(DeviceInfo).session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
