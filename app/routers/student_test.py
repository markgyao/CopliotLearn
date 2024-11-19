from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import student_test as crud_student_test
from app.schemas import student_test as schema_student_test
from app.db import get_db

router = APIRouter()

@router.post("/students_tests/", response_model=schema_student_test.StudentTest)
def create_student_test(student_test: schema_student_test.StudentTestCreate, db: Session = Depends(get_db)):
    return crud_student_test.create_student_test(db, student_test)

@router.get("/students_tests", response_model=list[schema_student_test.StudentTest])
def get_all_student_tests(db: Session = Depends(get_db)):
    return crud_student_test.get_all_student_tests(db)

@router.get("/students_tests/{student_id}/{test_id}", response_model=schema_student_test.StudentTest)
def get_student_test(student_id: int, test_id: int, db: Session = Depends(get_db)):
    db_student_test = crud_student_test.get_student_test(db, student_id, test_id)
    if db_student_test is None:
        raise HTTPException(status_code=404, detail="StudentTest not found")
    return db_student_test

@router.delete("/students_tests/{student_id}/{test_id}")
def delete_student_test(student_id: int, test_id: int, db: Session = Depends(get_db)):
    return crud_student_test.delete_student_test(db, student_id, test_id)