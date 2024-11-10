from fastapi import FastAPI, Depends
from ..api.v1.endpoints import endpoints
from dotenv import load_dotenv
import os

app = FastAPI()

app.include_router(endpoints.router)

@app.get('/')
def health_check():
    return "Ok, its working"