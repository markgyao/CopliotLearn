from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import student_homework as crud_student_homework
from app.schemas import student_homework as schema_student_homework
from app.db import get_db

router = APIRouter()

# Create a new student homework record
@router.post("/students_homeworks/", response_model=schema_student_homework.StudentHomework)
def create_student_homework(student_homework: schema_student_homework.StudentHomeworkCreate, db: Session = Depends(get_db)):
    return crud_student_homework.create_student_homework(db, student_homework)

# Get all student homework records
@router.get("/students_homeworks", response_model=list[schema_student_homework.StudentHomework])
def get_all_student_homeworks(db: Session = Depends(get_db)):
    return crud_student_homework.get_all_student_homeworks(db)

# Get a specific student homework record by student_id and homework_id
@router.get("/students_homeworks/{student_id}/{homework_id}", response_model=schema_student_homework.StudentHomework)
def get_student_homework(student_id: int, homework_id: int, db: Session = Depends(get_db)):
    db_student_homework = crud_student_homework.get_student_homework(db, student_id, homework_id)
    if db_student_homework is None:
        raise HTTPException(status_code=404, detail="StudentHomework not found")
    return db_student_homework

# Delete a specific student homework record by student_id and homework_id
@router.delete("/students_homeworks/{student_id}/{homework_id}")
def delete_student_homework(student_id: int, homework_id: int, db: Session = Depends(get_db)):
    return crud_student_homework.delete_student_homework(db, student_id, homework_id)