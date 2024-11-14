from sqlalchemy import Column, Integer

from db.postgress_db.models import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
