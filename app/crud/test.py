# from sqlalchemy.orm import Session
# from app.models.test import Test
# from app.schemas.test import TestCreate

# # Create a new test record in the database
# def create_test(db: Session, test: TestCreate):
#     db_test = Test(**test.dict())
#     db.add(db_test)
#     db.commit()
#     db.refresh(db_test)
#     return db_test

# # Retrieve a test record by its ID
# def get_test(db: Session, test_id: int):
#     return db.query(Test).filter(Test.id == test_id).first()

# # Retrieve all test records
# def get_all_tests(db: Session):
#     return db.query(Test).all()

# # Retrieve a limited number of test records with optional offset
# def get_tests(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(Test).offset(skip).limit(limit).all()

# # Delete a test record by its ID
# def delete_test(db: Session, test_id: int):
#     db_test = get_test(db, test_id)
#     if db_test:
#         db.delete(db_test)
#         db.commit()
#     return db_test