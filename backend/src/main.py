from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.src.authentications.routers import router as auth_router
from backend.src.database import Base, engine
from backend.src.dependency import has_access
from backend.src.drinks.models import Drink, IngredientNeeded  # noqa F401
from backend.src.orders.models import BarOrder  # noqa F401
from backend.src.storage.models import IngredientStorage  # noqa F401
from backend.src.users.models import User  # noqa F401
from backend.src.users.routers import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
    ],
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
async def home() -> dict[str, str]:
    return {
        "message": "redoc - http://localhost:5000/redoc \n swagger - http://localhost:5000/docs"
    }
