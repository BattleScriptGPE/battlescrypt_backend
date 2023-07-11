from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL
import logging
import os
import urllib


## SQL URL
url_object = URL.create(
    "mysql+pymysql",
    username=os.environ["DB_USER"],
    password=urllib.parse.quote(os.environ["DB_PASSWORD"]),
    host=os.environ["DB_URL"],
    port=int(os.environ["DB_PORT"]),
    database=os.environ["DB_NAME"],
)

print(url_object)

Base = declarative_base()




def get_db():
    try:
        engine = create_engine(url_object)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        logging.info(" [SQL] : Connect to DB Ok")
        return db
    except:
        logging.info(" [SQL] : Connect to DB Failed")
        db.close()
