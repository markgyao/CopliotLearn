
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Date
from app.db import Base

class StudentsHomeworks(Base):
    __tablename__ = "students_homeworks"

    student_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    homework_id = Column(Integer, ForeignKey("homeworks.id"), primary_key=True)
    grade = Column(DECIMAL(5, 2), nullable=False)
    submitted_date = Column(Date, nullable=False)