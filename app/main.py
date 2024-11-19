from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, class_schedules, class_routers, class_schedules, gallery, homework, permissions,role_permissions, student_homeworks,student_test,students,test,test_categories,user,role
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

print(f"SECRET_KEY: {SECRET_KEY}")  # Should not be None
print(f"DATABASE_URL: {DATABASE_URL}")  # Should not be None

# Initialize FastAPI app
app = FastAPI()

@app.get('/')
def lol():
    return {"wrong one ": "go to docs already"}

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
app.include_router(students.router)
app.include_router(auth.router)
app.include_router(class_schedules.router)
app.include_router(class_routers.router)
app.include_router(gallery.router)
app.include_router(homework.router)
app.include_router(permissions.router)
app.include_router(role_permissions.router)
app.include_router(student_homeworks.router)
app.include_router(student_test.router)
app.include_router(test.router)
app.include_router(test_categories.router)


#note: hardcoded-credentials Embedding credentials in source code risks unauthorized access