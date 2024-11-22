from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()

# Correct path to templates directory
templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
templates = Jinja2Templates(directory=templates_dir)

@router.get("/auth/{role}-login", response_class=HTMLResponse)
def login_page(role: str, request: Request):
    if role not in ["student", "teacher", "admin"]:
        return HTMLResponse("Invalid role", status_code=400)
    return templates.TemplateResponse(f"{role}_login.html", {"request": request})

@router.post("/auth/{role}-login", response_class=HTMLResponse)
def login(role: str, request: Request, username: str = Form(...), password: str = Form(...)):
    if role not in ["student", "teacher", "admin"]:
        return HTMLResponse("Invalid role", status_code=400)

    # Hardcoded credentials for testing
    if username == "testuser" and password == "password123" and role == "student":
        return templates.TemplateResponse(
            f"{role}_login.html", {"request": request, "message": "Welcome, testuser!"}
        )
    elif username == "testteacher" and password == "password123" and role == "teacher":
        return templates.TemplateResponse(
            f"{role}_login.html", {"request": request, "message": "Welcome, testteacher!"}
        )
    elif username == "testadmin" and password == "password123" and role == "admin":
        return templates.TemplateResponse(
            f"{role}_login.html", {"request": request, "message": "Welcome, testadmin!"}
        )

    # Invalid credentials
    return templates.TemplateResponse(
        f"{role}_login.html", {"request": request, "error": "Invalid credentials"}
    )
