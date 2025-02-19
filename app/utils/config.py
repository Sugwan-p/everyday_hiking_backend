import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings(BaseSettings):
    """✅ 환경 변수 관리"""
    APP_NAME: str = os.getenv("APP_NAME", "Everyday Hiking Backend")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")

    # Firebase 설정
    FIREBASE_CREDENTIALS: str = os.getenv("FIREBASE_CREDENTIALS")  # Firebase 서비스 계정 JSON 경로

    # Supabase 설정
    SUPABASE_USER: str = os.getenv("SUPABASE_USER")
    SUPABASE_PASSWORD: str = os.getenv("SUPABASE_PASSWORD")
    SUPABASE_DB: str = os.getenv("SUPABASE_DB")
    SUPABASE_HOST: str = os.getenv("SUPABASE_HOST", "localhost")
    SUPABASE_PORT: str = os.getenv("SUPABASE_PORT", "5432")

    DATABASE_URL: str = f"postgresql+psycopg2://{SUPABASE_USER}:{SUPABASE_PASSWORD}@{SUPABASE_HOST}:{SUPABASE_PORT}/{SUPABASE_DB}"
    # SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
    
    # JWT 설정
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your_secret_key")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))

settings = Settings()
