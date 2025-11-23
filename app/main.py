import logging
import logging.config
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import spells, dashboard, users
from app.data.logging_config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

app = FastAPI(title="Ministry of Magic System")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(spells.router)
app.include_router(dashboard.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Ministry System Online. Go to /static/index.html"}