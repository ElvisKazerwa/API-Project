from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, users, auth, vote
from .config import settings


print(settings.database_password)

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://WWW.google.com", "https://WWW.youtube.com"]

#for public ip address

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

#request Get Method url: "/"

@app.get("/")
def root():
    return {"message": "Welcome to my Api project!"}


  


