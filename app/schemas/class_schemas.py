from pydantic import BaseModel
from typing import Optional
from datetime import date

class ClassBase(BaseModel):
    name: str
    teacher_id: Optional[int] = None
    starting_date: date
    ending_date: date
    descriptions: Optional[str] = None
    subject: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int

    class Config:
        orm_mode = True