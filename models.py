from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Clothes(Base):
    __tablename__ = "clothes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    size = Column(String)
    color = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))

    category = relationship("Category", back_populates="items")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

    items = relationship("Clothes", back_populates="category")