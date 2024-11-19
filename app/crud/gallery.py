from sqlalchemy.orm import Session
from app.models.gallery import Gallery
from app.schemas.gallery import GalleryCreate

# Create a new gallery record in the database
def create_gallery(db: Session, gallery: GalleryCreate):
    db_gallery = Gallery(**gallery.dict())
    db.add(db_gallery)
    db.commit()
    db.refresh(db_gallery)
    return db_gallery

# Retrieve a gallery record by its image ID
def get_gallery(db: Session, image_id: int):
    return db.query(Gallery).filter(Gallery.image_id == image_id).first()

# Retrieve all gallery records
def get_all_galleries(db: Session):
    return db.query(Gallery).all()

# Retrieve a limited number of gallery records with optional offset
def get_galleries(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Gallery).offset(skip).limit(limit).all()

# Delete a gallery record by its image ID
def delete_gallery(db: Session, image_id: int):
    db_gallery = get_gallery(db, image_id)
    if db_gallery:
        db.delete(db_gallery)
        db.commit()
    return db_gallery