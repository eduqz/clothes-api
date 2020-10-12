from typing import List, Optional

from pydantic import BaseModel


class ClothesBase(BaseModel):
    name: str
    description: Optional[str] = None
    size: Optional[str] = None
    color: Optional[str] = None


class ClothesCreate(ClothesBase):
    category_id: int


class Clothes(ClothesBase):
    id: int

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    items: List[Clothes] = []

    class Config:
        orm_mode = True