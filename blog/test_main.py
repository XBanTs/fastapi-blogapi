from fastapi import FastAPI
from . import models
from .database import engine

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Hello World"}
