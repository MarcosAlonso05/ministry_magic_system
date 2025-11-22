from fastapi import FastAPI
from app.routers import spells

app = FastAPI(title="Ministry of Magic")

app.include_router(spells.router)

@app.get("/")
def read_root():
    return {"message": "Ministry System Online"}