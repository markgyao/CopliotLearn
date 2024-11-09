from fastapi import FastAPI
from app.routers import role, user, student, auth
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")
SECRET_KEY=os.getenv("SECRET_KEY")


app = FastAPI()

app.include_router(role.router)
app.include_router(user.router)
app.include_router(student.router)
app.include_router(auth.router)
