from pydantic import BaseModel
from datetime import date

class StudentHomeworkBase(BaseModel):
    student_id: int
    homework_id: int
    grade: float
    submitted_date: date

class StudentHomeworkCreate(StudentHomeworkBase):
    pass

class StudentHomework(StudentHomeworkBase):
    class Config:
        orm_mode = True