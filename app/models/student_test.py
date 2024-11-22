# from sqlalchemy import Column, Integer, ForeignKey, Date, DECIMAL
# from app.db import Base

# class StudentTest(Base):
#     __tablename__ = "students_tests"

#     student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, index=True)
#     test_id = Column(Integer, ForeignKey("tests.id", ondelete="CASCADE"), primary_key=True, index=True)
#     test_date = Column(Date, nullable=False)
#     test_score = Column(DECIMAL(5, 2), nullable=False)