from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    student_id: int
    grade_level: str
    main_parent_id: int
    secondary_parent_id: Optional[int] = None
    addional_info: Optional[str] = None
    food_allergy: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True