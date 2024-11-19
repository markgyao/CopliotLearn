from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import homework as crud_homework
from app.schemas import homework as schema_homework
from app.db import get_db

router = APIRouter()

@router.post("/homeworks/", response_model=schema_homework.Homework)
def create_homework(homework: schema_homework.HomeworkCreate, db: Session = Depends(get_db)):
    return crud_homework.create_homework(db, homework)

@router.get("/homeworks", response_model=list[schema_homework.Homework])
def get_all_homeworks(db: Session = Depends(get_db)):
    return crud_homework.get_all_homeworks(db)

@router.get("/homeworks/{homework_id}", response_model=schema_homework.Homework)
def get_homework(homework_id: int, db: Session = Depends(get_db)):
    db_homework = crud_homework.get_homework(db, homework_id)
    if db_homework is None:
        raise HTTPException(status_code=404, detail="Homework not found")
    return db_homework

@router.delete("/homeworks/{homework_id}")
def delete_homework(homework_id: int, db: Session = Depends(get_db)):
    return crud_homework.delete_homework(db, homework_id)