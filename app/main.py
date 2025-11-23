import logging
import logging.config
from fastapi import FastAPI
from app.routers import spells
from app.data.logging_config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

app = FastAPI(title="Ministry of Magic")

app.include_router(spells.router)

@app.get("/")
def read_root():
    return {"message": "Ministry System Online"}