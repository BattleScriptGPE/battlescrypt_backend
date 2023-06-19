from datatime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime, Text, Time
from sqlalchemy.orm import relationship

from app.utils.database_utils import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String,  index=True)
    age = Column(Integer, index=True)
    mail = Column(String, unique=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
    time_played = Column(Time, default=0)
    wins = Column(Integer, default=0)
    defeats = Column(Integer, default=0)
    line_coded = Column(Integer, default=0)
    last_connexion = Column(Time, default=0)
    experience = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    quests = relationship("UserQuests", back_populates="user")
    achievements = relationship("UserQuests", back_populates="user")
    