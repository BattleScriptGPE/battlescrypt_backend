from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime, Text, Time
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from typing import List

from app.utils.database_utils import Base

class UserAchievements(Base):
    __tablename__ = "user_achievements"
    id = Column(Integer, primary_key=True, index=True)
    id_quest = Column(Integer, ForeignKey("achievement.id"))
    id_user = Column(Integer, ForeignKey("user.id"))
    done_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="achievements")
    quests = relationship("Achievement", back_populates="achievement")
    