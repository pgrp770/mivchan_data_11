from sqlalchemy import Column, Integer

from db.postgress_db.models import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.postgress_db.models import Base


class SuspiciousHostageContent(Base):
    __tablename__ = "suspicious_hostage_content"
    id = Column(Integer, primary_key=True, autoincrement=True)

    sentence = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="sentences_hostage")
