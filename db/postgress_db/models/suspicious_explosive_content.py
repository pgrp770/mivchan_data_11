from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.postgress_db.models import Base


class SuspiciousExplosiveContent(Base):
    __tablename__ = "suspicious_explosive_contents"
    id = Column(Integer, primary_key=True, autoincrement=True)

    ip_address = Column(String)
    created_at = Column(String)

    device_info_id = Column(Integer, ForeignKey("devices_info.id"))


    sentences_id = Column(Integer, ForeignKey("user.id"))


