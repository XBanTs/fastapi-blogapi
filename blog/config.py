import os
from typing import Optional

class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    
    # For production, use PostgreSQL
    @property
    def database_url(self) -> str:
        if self.DATABASE_URL:
            # Render provides DATABASE_URL, but we need to handle postgres:// vs postgresql://
            if self.DATABASE_URL.startswith("postgres://"):
                # Convert to postgresql+psycopg:// to use psycopg3
                return self.DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)
            elif self.DATABASE_URL.startswith("postgresql://"):
                # Convert to postgresql+psycopg:// to use psycopg3
                return self.DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)
            return self.DATABASE_URL
        # Fallback to SQLite for local development
        import os
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        return f'sqlite:///{os.path.join(BASE_DIR, "blog.db")}'

settings = Settings()