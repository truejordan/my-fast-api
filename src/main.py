from fastapi import FastAPI
from .routers.speakers.speakers import router as speakers_router
from .routers.talks.talks import router as talks_router
from .routers.math.math import router as math_router
from .database.database import Base, engine

# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Included routers
app.include_router(speakers_router)
app.include_router(talks_router)
app.include_router(math_router)