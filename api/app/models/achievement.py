from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime, Text, Time
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from typing import List

from app.utils.data import Base

class Achievement(Base):
    __tablename__ = "achievement"
    id = Column(Integer, primary_key=True, index=True)
    xp = Column(Integer, unique=True, index=True)
    description = Column(Text, unique=True, index=True)
    metas = Column(Text, unique=True, index=True)

    achievement = relationship("UserAchievements", back_populates="achievements")
    