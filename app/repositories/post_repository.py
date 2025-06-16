from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate

class PostRepository:
    async def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Post).offset(skip).limit(limit).all()
    
    async def get_by_id(self, db: Session, post_id: int):
        return db.query(Post).filter(Post.id == post_id).first()
    
    async def create(self, db: Session, post: PostCreate):
        db_post = Post(**post.dict())
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post
    
    async def update(self, db: Session, post_id: int, post: PostUpdate):
        db_post = await self.get_by_id(db, post_id)
        if not db_post:
            return None
            
        for key, value in post.dict(exclude_unset=True).items():
            setattr(db_post, key, value)
            
        db.commit()
        db.refresh(db_post)
        return db_post
    
    async def delete(self, db: Session, post_id: int):
        db_post = self.get_by_id(db, post_id)
        if not db_post:
            return False
            
        db.delete(db_post)
        db.commit()
        return True 