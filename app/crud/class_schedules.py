from sqlalchemy.orm import Session
from app.models.class_schedule import ClassSchedule
from app.schemas.class_schedule import ClassScheduleCreate

def create_class_schedule(db: Session, class_schedule: ClassScheduleCreate):
    db_class_schedule = ClassSchedule(**class_schedule.dict())
    db.add(db_class_schedule)
    db.commit()
    db.refresh(db_class_schedule)
    return db_class_schedule

def get_class_schedule(db: Session, class_id: int, day_of_week: str, start_time: str, end_time: str):
    return db.query(ClassSchedule).filter(ClassSchedule.class_id == class_id, ClassSchedule.day_of_week == day_of_week, ClassSchedule.start_time == start_time, ClassSchedule.end_time == end_time).first()

def get_all_class_schedules(db: Session):
    return db.query(ClassSchedule).all()

def delete_class_schedule(db: Session, class_id: int, day_of_week: str, start_time: str, end_time: str):
    db_class_schedule = get_class_schedule(db, class_id, day_of_week, start_time, end_time)
    if db_class_schedule:
        db.delete(db_class_schedule)
        db.commit()
    return db_class_schedule