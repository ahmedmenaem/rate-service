from fastapi import FastAPI, Query
from app.routes import rates

app = FastAPI()

app.include_router(rates.router, prefix="/rate", tags=['rates'])
