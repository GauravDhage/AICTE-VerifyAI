
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers.api import router
from .routers.tracking import router as tracking_router

Base.metadata.create_all(engine)

app = FastAPI(title="AICTE Official Scrutiny Portal")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://aicte-verifyai-kohl.vercel.app",
]

extra_origins = os.getenv("VERIFYAI_CORS", "")
origins.extend(
    origin.strip().rstrip("/")
    for origin in extra_origins.split(",")
    if origin.strip()
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=list(set(origins)),
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(router)
app.include_router(tracking_router)
