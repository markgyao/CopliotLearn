# from sqlalchemy.orm import Session
# from app.models.student_test import StudentTest
# from app.schemas.student_test import StudentTestCreate

# # Create a new student test record in the database
# def create_student_test(db: Session, student_test: StudentTestCreate):
#     db_student_test = StudentTest(**student_test.dict())
#     db.add(db_student_test)
#     db.commit()
#     db.refresh(db_student_test)
#     return db_student_test

# # Retrieve a student test record by student ID and test ID
# def get_student_test(db: Session, student_id: int, test_id: int):
#     return db.query(StudentTest).filter(StudentTest.student_id == student_id, StudentTest.test_id == test_id).first()

# # Retrieve all student test records
# def get_all_student_tests(db: Session):
#     return db.query(StudentTest).all()

# # Delete a student test record by student ID and test ID
# def delete_student_test(db: Session, student_id: int, test_id: int):
#     db_student_test = get_student_test(db, student_id, test_id)
#     if db_student_test:
#         db.delete(db_student_test)
#         db.commit()
#     return db_student_test