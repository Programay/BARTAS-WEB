from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .dependency import has_access
from .users import models
from .users.routers import router as users_router
from .authentications.routers import router as auth_router
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Routers
PROTECTED = [Depends(has_access)]

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
async def home():
    return {"message": "http://localhost:5000/redoc"}
