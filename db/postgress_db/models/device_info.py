from sqlalchemy import Column, Integer

from db.postgress_db.models import Base


class DeviceInfo(Base):
    __tablename__ = "devices_info"
    id = Column(Integer, primary_key=True, autoincrement=True)