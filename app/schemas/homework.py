from pydantic import BaseModel
from typing import Optional
from datetime import date

class HomeworkBase(BaseModel):
    name: str
    class_id: int
    description: Optional[str] = None
    homework_content: Optional[str] = None
    due_date: Optional[date] = None
    file_path: Optional[str] = None
    answer_key_path: Optional[str] = None
    grade_level: Optional[str] = None

class HomeworkCreate(HomeworkBase):
    pass

class Homework(HomeworkBase):
    id: int

    class Config:
        orm_mode = True