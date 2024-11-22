# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.crud import test_categories as crud_test_categories
# from app.schemas import test_category as schema_test_category
# from app.db import get_db
# from app.schemas import user as schema_user
# from app.routers.auth import get_current_user
# from app.utils.permissions import has_permission

# router = APIRouter()

# @router.post("/test_categories/", response_model=schema_test_category.TestCategory)
# def create_test_category(
#     test_category: schema_test_category.TestCategoryCreate, 
#     db: Session = Depends(get_db), 
#     current_user: schema_user.User = Depends(get_current_user)
# ):
#     if not has_permission(current_user.role_id, "test_categories", "create"):
#         raise HTTPException(status_code=403, detail="Not enough permissions")
#     return crud_test_categories.create_test_category(db, test_category)

# @router.get("/test_categories", response_model=list[schema_test_category.TestCategory])
# def get_all_test_categories(
#     db: Session = Depends(get_db), 
#     current_user: schema_user.User = Depends(get_current_user)
# ):
#     if not has_permission(current_user.role_id, "test_categories", "read"):
#         raise HTTPException(status_code=403, detail="Not enough permissions")
#     return crud_test_categories.get_all_test_categories(db)

# @router.get("/test_categories/{test_category_id}", response_model=schema_test_category.TestCategory)
# def get_test_category(
#     test_category_id: int, 
#     db: Session = Depends(get_db), 
#     current_user: schema_user.User = Depends(get_current_user)
# ):
#     if not has_permission(current_user.role_id, "test_categories", "read"):
#         raise HTTPException(status_code=403, detail="Not enough permissions")
#     db_test_category = crud_test_categories.get_test_category(db, test_category_id)
#     if db_test_category is None:
#         raise HTTPException(status_code=404, detail="TestCategory not found")
#     return db_test_category

# @router.delete("/test_categories/{test_category_id}")
# def delete_test_category(
#     test_category_id: int, 
#     db: Session = Depends(get_db), 
#     current_user: schema_user.User = Depends(get_current_user)
# ):
#     if not has_permission(current_user.role_id, "test_categories", "delete"):
#         raise HTTPException(status_code=403, detail="Not enough permissions")
#     return crud_test_categories.delete_test_category(db, test_category_id)