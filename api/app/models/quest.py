from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.utils.database_utils import Base

class Quest(Base):
    __tablename__ = "quest"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    number = Column(Integer, unique=True, nullable=False)
    description = Column(Text, unique=True, index=True)
    difficulty = Column(Integer, default=0, nullable=False)
    xp = Column(Integer, unique=True, index=True)

    quest = relationship("UserQuests", back_populates="quests")
    