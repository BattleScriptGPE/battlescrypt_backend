from fastapi import FastAPI
from app.router import router
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

app = FastAPI()


## active when prod deploi
#app = FastAPI(
#    docs_url=None, # Disable docs (Swagger UI)
#    redoc_url=None, # Disable redoc
#)


logging.basicConfig(level=logging.INFO)
origins = [
    "http://localhost",
    "http://localhost:8080",
]
url_object = "mysql+pymysql://{}:{}@{}:{}/{}".format(os.environ["DB_USER"],os.environ["DB_PASSWORD"], os.environ["DB_URL"], os.environ["DB_PORT"], os.environ["DB_NAME"])
logging.INFO(url_object)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.router)
