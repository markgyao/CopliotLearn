# from sqlalchemy.orm import Session
# from app.models.student_homework import StudentHomework
# from app.schemas.student_homework import StudentHomeworkCreate

# # Create a new student homework record in the database
# def create_student_homework(db: Session, student_homework: StudentHomeworkCreate):
#     db_student_homework = StudentHomework(**student_homework.dict())
#     db.add(db_student_homework)
#     db.commit()
#     db.refresh(db_student_homework)
#     return db_student_homework

# # Retrieve a student homework record by student ID and homework ID
# def get_student_homework(db: Session, student_id: int, homework_id: int):
#     return db.query(StudentHomework).filter(StudentHomework.student_id == student_id, StudentHomework.homework_id == homework_id).first()

# # Retrieve all student homework records
# def get_all_student_homeworks(db: Session):
#     return db.query(StudentHomework).all()

# # Delete a student homework record by student ID and homework ID
# def delete_student_homework(db: Session, student_id: int, homework_id: int):
#     db_student_homework = get_student_homework(db, student_id, homework_id)
#     if db_student_homework:
#         db.delete(db_student_homework)
#         db.commit()
#     return db_student_homework