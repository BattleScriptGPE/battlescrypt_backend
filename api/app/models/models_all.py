from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime, Text, Time
from sqlalchemy.orm import relationship

from app.utils.database_utils import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
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


class UserQuests(Base):
    __tablename__ = "user_quests"
    id = Column(Integer, primary_key=True, index=True)
    id_quest = Column(Integer, ForeignKey("quest.id"))
    id_user = Column(Integer, ForeignKey("user.id"))
    status = Column(Enum)
    code = Column(Text, nullable=True)
    done_at = Column(DateTime, nullable=True)


class Quest(Base):
    __tablename__ = "quest"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    number = Column(Integer, unique=True, nullable=False)
    description = Column(Text, unique=True, index=True)
    difficulty = Column(Integer, default=0, nullable=False)
    xp = Column(Integer, unique=True, index=True)


class Achievement(Base):
    __tablename__ = "achievement"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=True)
    xp_value = Column(Integer, unique=True, index=True)
    description = Column(Text, unique=True, index=True)
    metas = Column(Text, unique=True, index=True)


class UserAchievements(Base):
    __tablename__ = "user_achievements"
    id = Column(Integer, primary_key=True, index=True)
    id_achievement = Column(Integer)
    id_user = Column(Integer)
    done_at = Column(DateTime, nullable=True)
