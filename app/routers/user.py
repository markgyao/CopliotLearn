from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.schemas import user as schema_user
from app.db import get_db
from app.routers.auth import get_current_user
from app.utils.permissions import has_permission

router = APIRouter()

# Create a new user
@router.post("/users/", response_model=schema_user.User)
def create_user(
    user: schema_user.UserCreate, 
    db: Session = Depends(get_db), 
    current_user: schema_user.User = Depends(get_current_user)
):
    if not has_permission(current_user.role_id, "users", "create"):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return crud_user.create_user(db, user)

# Get all users
@router.get("/users", response_model=list[schema_user.User])
def get_all_users(
    db: Session = Depends(get_db), 
    current_user: schema_user.User = Depends(get_current_user)
):
    if not has_permission(current_user.role_id, "users", "read"):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    users = crud_user.get_all_users(db)
    return users

# Get a specific user by ID
@router.get("/users/{user_id}", response_model=schema_user.User)
def get_user(
    user_id: int, 
    db: Session = Depends(get_db), 
    current_user: schema_user.User = Depends(get_current_user)
):
    # Allow access if the user is accessing their own data
    if current_user.id != user_id and not has_permission(current_user.role_id, "users", "read"):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_user = crud_user.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Delete a specific user by ID
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int, 
    db: Session = Depends(get_db), 
    current_user: schema_user.User = Depends(get_current_user)
):
    if not has_permission(current_user.role_id, "users", "delete"):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return crud_user.delete_user(db, user_id)
