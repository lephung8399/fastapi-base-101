from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.models.base import get_db
from app.schemas.post import Post, PostCreate, PostUpdate
from app.services.post_service import PostService

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

post_service = PostService()

@router.get("/", response_model=List[Post])
async def get_posts(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await post_service.get_posts(db, skip, limit)

@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: int, db: AsyncSession = Depends(get_db)):
    return await post_service.get_post(db, post_id)

@router.post("/", response_model=Post)
async def create_post(post: PostCreate, db: AsyncSession = Depends(get_db)):
    return await post_service.create_post(db, post)

@router.put("/{post_id}", response_model=Post)
async def update_post(post_id: int, post: PostUpdate, db: AsyncSession = Depends(get_db)):
    return await post_service.update_post(db, post_id, post)

@router.delete("/{post_id}")
async def delete_post(post_id: int, db: AsyncSession = Depends(get_db)):
    return await post_service.delete_post(db, post_id)
