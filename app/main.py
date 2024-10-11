from fastapi import FastAPI
from app.routers import role, user, student



app = FastAPI()

app.include_router(role.router)
app.include_router(user.router)
app.include_router(student.router)
