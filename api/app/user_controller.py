from sqlalchemy.orm import Session
import models, schemas
import hashlib

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_mail(db: Session, mail: str):
    return db.query(models.User).filter(models.User.mail == mail).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hashlib.md5(user.password.encode())
    db_user = models.User(lastname=user.lastname,
                        firstname=user.firstname,
                        age=user.age,
                        username=user.username,
                        mail=user.mail,
                        password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
