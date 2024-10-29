from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.schemas import user as schema_user
from app.db import get_db

router = APIRouter()

@router.post("/users/", response_model=schema_user.User)
def create_user(user: schema_user.UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, user)

# New route to get all users
@router.get("/users", response_model=list[schema_user.User])
def get_all_users(db: Session = Depends(get_db)):
    users = crud_user.get_all_users(db)
    return users

@router.get("/users/{user_id}", response_model=schema_user.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud_user.delete_user(db, user_id)
