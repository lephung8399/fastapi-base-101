from sqlalchemy import func, Column, DateTime, Boolean, Integer

from app.models.base import Base


class ModelBase(Base):

    __abstract__ = True

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
    del_flag = Column(Boolean, nullable=False, default=False) # del_flag = True is deleted