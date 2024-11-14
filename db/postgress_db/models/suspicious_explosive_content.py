from sqlalchemy import Column, Integer

from db.postgress_db.models import Base


class SuspiciousExplosiveContent(Base):
    __tablename__ = "suspicious_explosive_contents"
    id = Column(Integer, primary_key=True, autoincrement=True)
