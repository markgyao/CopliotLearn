# from sqlalchemy.orm import Session
# from app.models.test_category import TestCategory
# from app.schemas.test_category import TestCategoryCreate

# # Create a new test category record in the database
# def create_test_category(db: Session, test_category: TestCategoryCreate):
#     db_test_category = TestCategory(**test_category.dict())
#     db.add(db_test_category)
#     db.commit()
#     db.refresh(db_test_category)
#     return db_test_category

# # Retrieve a test category record by its ID
# def get_test_category(db: Session, test_category_id: int):
#     return db.query(TestCategory).filter(TestCategory.id == test_category_id).first()

# # Retrieve all test category records
# def get_all_test_categories(db: Session):
#     return db.query(TestCategory).all()

# # Retrieve a limited number of test category records with optional offset
# def get_test_categories(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(TestCategory).offset(skip).limit(limit).all()

# # Delete a test category record by its ID
# def delete_test_category(db: Session, test_category_id: int):
#     db_test_category = get_test_category(db, test_category_id)
#     if db_test_category:
#         db.delete(db_test_category)
#         db.commit()
#     return db_test_category