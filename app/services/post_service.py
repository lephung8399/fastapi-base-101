from sqlalchemy.orm import Session
from app.schemas.post import PostCreate, PostUpdate
from app.repositories.post_repository import PostRepository
from fastapi import HTTPException


class PostService:
    def __init__(self):
        self.repository = PostRepository()

    async def get_posts(self, db: Session, skip: int = 0, limit: int = 100):
        return await self.repository.get_all(db, skip, limit)

    async def get_post(self, db: Session, post_id: int):
        post = await self.repository.get_by_id(db, post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

    async def create_post(self, db: Session, post: PostCreate):
        # Add any business logic here before creating post
        return await self.repository.create(db, post)

    async def update_post(self, db: Session, post_id: int, post: PostUpdate):
        updated_post = await self.repository.update(db, post_id, post)
        if not updated_post:
            raise HTTPException(status_code=404, detail="Post not found")
        return updated_post

    async def delete_post(self, db: Session, post_id: int):
        if not await self.repository.delete(db, post_id):
            raise HTTPException(status_code=404, detail="Post not found")
        return {"message": "Post deleted successfully"}
