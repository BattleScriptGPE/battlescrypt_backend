from fastapi import FastAPI
from app.router import router
from fastapi.middleware.cors import CORSMiddleware
import logging

#app = FastAPI()

## active when prod deploi
app = FastAPI(
    docs_url=None, # Disable docs (Swagger UI)
    redoc_url=None, # Disable redoc
)


logging.basicConfig(level=logging.INFO)
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.router)
