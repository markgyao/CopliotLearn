
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Date
from app.db import Base

class StudentsTests(Base):
    __tablename__ = "students_tests"

    student_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    test_id = Column(Integer, ForeignKey("tests.id"), primary_key=True)
    test_date = Column(Date, nullable=False)
    test_score = Column(DECIMAL(5, 2), nullable=False)