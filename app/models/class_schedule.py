# from sqlalchemy import Column, Integer, String, Time, ForeignKey
# from app.db import Base

# class ClassSchedule(Base):
#     __tablename__ = "class_schedules"

#     class_id = Column(Integer, ForeignKey("classes.id", ondelete="CASCADE"), primary_key=True, index=True)
#     day_of_week = Column(String(10), primary_key=True, nullable=False)
#     start_time = Column(Time, primary_key=True, nullable=False)
#     end_time = Column(Time, primary_key=True, nullable=False)