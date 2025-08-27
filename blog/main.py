from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI(
    title="Blog API",
    description="A FastAPI blog application with JWT authentication",
    version="1.0.0"
)

# CORS middleware for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

@app.on_event("startup")
async def startup_event():
    # Create database tables only when the app starts, not during build
    models.Base.metadata.create_all(engine)

@app.get("/")
def root():
    return {"message": "Blog API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}