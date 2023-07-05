from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
import sqlalchemy
import os


## SQL URL
engine = create_engine('mysql+pymysql://' + os.environ["DB_USER"] + ':' + os.environ["DB_PASSWORD"] + '@' + os.environ["DB_URL"] + ':' + os.environ["DB_PORT"] + '/' + os.environ["DB_NAME"])
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        logging.info(" [SQL] : Connect to DB Ok")
        return db
    except:
        logging.info(" [SQL] : Connect to DB Failed")
        db.close()
