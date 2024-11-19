from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import test as crud_test
from app.schemas import test as schema_test
from app.db import get_db

router = APIRouter()

# Create a new test
@router.post("/tests/", response_model=schema_test.Test)
def create_test(test: schema_test.TestCreate, db: Session = Depends(get_db)):
    return crud_test.create_test(db, test)

# Get all tests
@router.get("/tests", response_model=list[schema_test.Test])
def get_all_tests(db: Session = Depends(get_db)):
    return crud_test.get_all_tests(db)

# Get a specific test by ID
@router.get("/tests/{test_id}", response_model=schema_test.Test)
def get_test(test_id: int, db: Session = Depends(get_db)):
    db_test = crud_test.get_test(db, test_id)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test

# Delete a specific test by ID
@router.delete("/tests/{test_id}")
def delete_test(test_id: int, db: Session = Depends(get_db)):
    return crud_test.delete_test(db, test_id)