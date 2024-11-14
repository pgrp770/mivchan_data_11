from sqlalchemy import Column, Integer

from db.postgress_db.models import Base


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, autoincrement=True)