from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    grade_level: str
    addional_info: Optional[str]
    food_allergy: Optional[str]

class StudentCreate(StudentBase):
    student_id: int
    main_parent_id: int
    secondary_parent_id: Optional[int]

class Student(StudentBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True
