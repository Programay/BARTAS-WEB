from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .dependency import has_access
from .users import models
from .users.routers import router as users_router
from .authentications.routers import router as auth_router
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
PROTECTED = [Depends(has_access)]

app.include_router(auth_router)
app.include_router(users_router, dependencies=PROTECTED)


@app.get("/")
async def home():
    return {"message": "Welcome home!"}
