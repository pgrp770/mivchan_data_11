from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.postgress_db.models import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)

    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(String)

    location = relationship("Location", back_populates="user")
    device = relationship("DeviceInfo", back_populates="user")

    sentences_explosive = relationship("SuspiciousExplosiveContent", back_populates="user")
    sentences_hostage = relationship("SuspiciousHostageContent", back_populates="user")