from sqlalchemy.orm import Session

import models
import schemas


def get_clothes(db: Session, clothes_id: int):
    return db.query(models.Clothes).filter(models.Clothes.id == clothes_id).first()


def get_clothes_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Clothes).offset(skip).limit(limit).all()


def create_clothes(db: Session, clothes: schemas.ClothesCreate):
    db_clothes = models.Clothes(name=clothes.name, description=clothes.description, size=clothes.size, color=clothes.color, category_id=clothes.category_id)
    db.add(db_clothes)
    db.commit()
    db.refresh(db_clothes)
    return db_clothes

def update_clothes(db: Session, clothes_id: int, clothes: schemas.ClothesCreate):
    db_clothes = db.query(models.Clothes).filter(models.Clothes.id == clothes_id).first()
    
    if (clothes.name):
        db_clothes.name = clothes.name
    
    if (clothes.description):
        db_clothes.description = clothes.description

    if (clothes.size):
        db_clothes.size = clothes.size

    if (clothes.color):
        db_clothes.color = clothes.color

    if (clothes.category_id):
        db_clothes.category_id = clothes.category_id

    db.commit()
    db.refresh(db_clothes)
    return db_clothes

def delete_clothes(db: Session, clothes_id: int):
    db_clothes = db.query(models.Clothes).filter(models.Clothes.id == clothes_id).delete()
    db.commit()

    return db_clothes


def get_category_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
