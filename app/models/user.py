from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models.model import ModelBase


class User(ModelBase):
    __tablename__ = "users"

    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255))
    activate = Column(Boolean, default=True)
    role = Column(Integer, nullable=False)

    posts = relationship("Post", back_populates="user")
