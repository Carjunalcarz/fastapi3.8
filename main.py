from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.util.init_db import create_tables
from app.routers.auth import authRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB at Start
    print("Created")
    create_tables()
    yield  # separation point


app = FastAPI(lifespan=lifespan)
app.include_router(router=authRouter, tags=["auth"], prefix="/auth")
# /auth/login
# /auth/singup


@app.get("/health")
def health_check():
    return {"status": "Running.... wazzap"}
