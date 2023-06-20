from sqlalchemy.orm import Session
from api.app.models.user import User
import hashlib
import api.app.utils.schemas as schemas

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_mail(db: Session, mail: str):
    return db.query(User).filter(User.mail == mail).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hashlib.md5(user.password.encode())
    db_user = User(lastname=user.lastname,
                          firstname=user.firstname,
                          age=user.age,
                          username=user.username,
                          mail=user.mail,
                          password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
