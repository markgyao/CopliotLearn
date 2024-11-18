
from sqlalchemy import Column, Integer, String, Time, ForeignKey
from app.db import Base

class ClassSchedules(Base):
    __tablename__ = "class_schedules"

    class_id = Column(Integer, ForeignKey("classes.id"), primary_key=True)
    day_of_week = Column(String(10), primary_key=True)
    start_time = Column(Time, primary_key=True)
    end_time = Column(Time, primary_key=True)