from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL
import logging
import os


## SQL URL
url_object = URL.create(
    "mariadb+pymysql",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_URL"],
    port=int(os.environ["DB_PORT"]),
    database=os.environ["DB_NAME"],
)





def get_db():
    try:
        print(url_object)
        engine = create_engine(url_object)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()
        db = SessionLocal()
        logging.info(" [SQL] : Connect to DB Ok")
        return db
    except:
        logging.info(" [SQL] : Connect to DB Failed")
        db.close()
