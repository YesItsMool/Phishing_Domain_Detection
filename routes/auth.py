from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
def register_post(request: Request):
    # Handle registration form submission here
    # Retrieve form data from request
    # Register user using the UserManager

    # Assuming the registration is successful, you can return a JSON response
    result = {"message": "Registration successful"}
    return JSONResponse(content=result)

@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login_post(request: Request):
    # Handle login form submission here
    # Retrieve form data from request
    # Check credentials using the UserManager

    # Assuming the login is successful, you can return a JSON response
    result = {"message": "Login successful"}
    return JSONResponse(content=result)

@router.get("/login_success")
def login_success(request: Request):
    return templates.TemplateResponse("login_success.html", {"request": request})
