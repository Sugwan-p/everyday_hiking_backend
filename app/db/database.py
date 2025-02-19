from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.utils.config import settings  # 환경 변수 가져오기

# SQLAlchemy 데이터베이스 연결
DATABASE_URL = settings.DATABASE_URL

Base = declarative_base()

# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DB 세션을 반환하는 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
