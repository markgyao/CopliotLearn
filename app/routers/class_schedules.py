from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import class_schedules as crud_class_schedules
from app.schemas import class_schedule as schema_class_schedule
from app.db import get_db

router = APIRouter()

# Create a new class schedule
@router.post("/class_schedules/", response_model=schema_class_schedule.ClassSchedule)
def create_class_schedule(class_schedule: schema_class_schedule.ClassScheduleCreate, db: Session = Depends(get_db)):
    return crud_class_schedules.create_class_schedule(db, class_schedule)

# Get all class schedules
@router.get("/class_schedules", response_model=list[schema_class_schedule.ClassSchedule])
def get_all_class_schedules(db: Session = Depends(get_db)):
    return crud_class_schedules.get_all_class_schedules(db)

# Get a specific class schedule by class_id, day_of_week, start_time, and end_time
@router.get("/class_schedules/{class_id}/{day_of_week}/{start_time}/{end_time}", response_model=schema_class_schedule.ClassSchedule)
def get_class_schedule(class_id: int, day_of_week: str, start_time: str, end_time: str, db: Session = Depends(get_db)):
    db_class_schedule = crud_class_schedules.get_class_schedule(db, class_id, day_of_week, start_time, end_time)
    if db_class_schedule is None:
        raise HTTPException(status_code=404, detail="Class Schedule not found")
    return db_class_schedule

# Delete a specific class schedule by class_id, day_of_week, start_time, and end_time
@router.delete("/class_schedules/{class_id}/{day_of_week}/{start_time}/{end_time}")
def delete_class_schedule(class_id: int, day_of_week: str, start_time: str, end_time: str, db: Session = Depends(get_db)):
    return crud_class_schedules.delete_class_schedule(db, class_id, day_of_week, start_time, end_time)