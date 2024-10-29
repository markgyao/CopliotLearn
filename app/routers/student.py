from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import student as crud_student
from app.schemas import student as schema_student
from app.db import get_db

router = APIRouter()

@router.post("/students/", response_model=schema_student.Student)
def create_student(student: schema_student.StudentCreate, db: Session = Depends(get_db)):
    return crud_student.create_student(db, student)

@router.get("/students/{student_id}", response_model=schema_student.Student)
def get_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud_student.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud_student.delete_student(db, student_id)
