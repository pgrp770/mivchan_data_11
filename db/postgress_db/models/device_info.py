from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.postgress_db.models import Base


class DeviceInfo(Base):
    __tablename__ = "devices_info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="device")
