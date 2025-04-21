from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.post import router as post_router


app = FastAPI(title="FastAPI Base Project")
app.include_router(post_router)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Base Project111"}
