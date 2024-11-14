from sqlalchemy import Column, Integer

from db.postgress_db.models import Base


class SuspiciousHostageContent(Base):
    __tablename__ = "suspicious_hostage_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
