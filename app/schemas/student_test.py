from pydantic import BaseModel
from datetime import date

class StudentTestBase(BaseModel):
    student_id: int
    test_id: int
    test_date: date
    test_score: float

class StudentTestCreate(StudentTestBase):
    pass

class StudentTest(StudentTestBase):
    class Config:
        orm_mode = True