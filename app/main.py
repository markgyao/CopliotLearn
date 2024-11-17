from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import role, user, student, auth
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routers
app.include_router(role.router)
app.include_router(user.router)
app.include_router(student.router)
app.include_router(auth.router)
