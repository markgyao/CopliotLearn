from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate

# Create a new student record in the database
def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Retrieve a student record by its ID
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

# Retrieve all student records
def get_all_students(db: Session):
    return db.query(Student).all()

# Retrieve a limited number of student records with optional offset
def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Student).offset(skip).limit(limit).all()

# Delete a student record by its ID
def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student