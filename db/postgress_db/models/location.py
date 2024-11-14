from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.postgress_db.models import Base


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(String)
    longitude = Column(String)
    city = Column(String)
    country = Column(String)

    user = relationship("User", back_populates="location")
