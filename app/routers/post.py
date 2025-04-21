from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.base import get_db
from app.schemas.post import Post, PostCreate, PostUpdate
from app.services.post_service import PostService

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

@router.get("/", response_model=List[Post])
def get_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return PostService.get_posts(db, skip, limit)

@router.get("/{post_id}", response_model=Post)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return PostService.get_post(db, post_id)
