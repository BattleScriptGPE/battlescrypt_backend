# main.py
from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
import user_controller, models, schemas
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm
from utils import (
    create_access_token,
    create_refresh_token,
    verify_password,
)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "API is currently working"}

@app.post("/register", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_controller.get_user_by_mail(db, mail=user.mail)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = user_controller.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return user_controller.create_user(db=db, user=user)

@app.post('/login', response_model=schemas.TokenSchema)
async def login(form_data: schemas.UserConnect, db: Session = Depends(get_db)): 
    user = user_controller.get_user_by_username(db, username=form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    #result = verify_password(password=form_data.password, hashed_password=user.password)
    if not verify_password(password=form_data.password, hashed_password=user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Incorrect email or passworrd {result} {user.password}"
        )
        
    return {
        "access_token": create_access_token(user.mail),
        "refresh_token": create_refresh_token(user.mail),
    }
