from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import sys
sys.path.append('./src')

import crud, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/clothes/", response_model=schemas.Clothes)
def create_clothes(clothes: schemas.ClothesCreate, db: Session = Depends(get_db)):
    return crud.create_clothes(db=db, clothes=clothes)


@app.get("/clothes/", response_model=List[schemas.Clothes])
def read_clothes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clothes = crud.get_clothes_list(db, skip=skip, limit=limit)
    return clothes


@app.get("/clothes/{clothes_id}", response_model=schemas.Clothes)
def read_clothes(clothes_id: int, db: Session = Depends(get_db)):
    db_clothes = crud.get_clothes(db, clothes_id=clothes_id)
    if db_clothes is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_clothes


@app.put("/clothes/{clothes_id}", response_model=schemas.Clothes)
def update_clothes(clothes_id: int, clothes: schemas.ClothesEdition, db: Session = Depends(get_db)):
    db_clothes = crud.get_clothes(db=db, clothes_id=clothes_id)

    if db_clothes is None:
        raise HTTPException(status_code=404, detail="User not found")

    print(db_clothes)
    
    return crud.update_clothes(db=db, clothes_id=clothes_id, clothes=clothes)


@app.delete("/clothes/{clothes_id}")
def delete_clothes(clothes_id: int, db: Session = Depends(get_db)):
    db_clothes = crud.get_clothes(db=db, clothes_id=clothes_id)
    if db_clothes is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.delete_clothes(db=db, clothes_id=clothes_id)


@app.post("/categories/", response_model=schemas.Category)
def create_category(
    category: schemas.CategoryCreate, db: Session = Depends(get_db)
):
    return crud.create_category(db=db, category=category)


@app.get("/categories/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_category_list(db, skip=skip, limit=limit)
    return categories