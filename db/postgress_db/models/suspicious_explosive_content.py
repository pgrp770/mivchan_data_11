from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.postgress_db.models import Base


class SuspiciousExplosiveContent(Base):
    __tablename__ = "suspicious_explosive_contents"
    id = Column(Integer, primary_key=True, autoincrement=True)

    sentence = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="sentences_explosive")
