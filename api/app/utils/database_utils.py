from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
import sqlalchemy
import os


## SQL URL
connect_url = sqlalchemy.engine.url.URL(
    "mysql+pymysql",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_URL"],
    port=os.environ["DB_PORT"],
    database=os.environ["DB_NAME"],
)

engine = create_engine(connect_url)
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
