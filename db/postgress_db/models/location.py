from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.postgress_db.models import Base


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(String)
    longitude = Column(String)
    city = Column(String)
    country = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="location")
