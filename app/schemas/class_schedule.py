from pydantic import BaseModel
from datetime import time

class ClassScheduleBase(BaseModel):
    class_id: int
    day_of_week: str
    start_time: time
    end_time: time

class ClassScheduleCreate(ClassScheduleBase):
    pass

class ClassSchedule(ClassScheduleBase):
    class Config:
        orm_mode = True