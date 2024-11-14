from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.postgress_db.models import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)

    email = Column(String)
    username = Column(String)

    location = relationship("Location", back_populates="user")
