from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.utils.config import settings
from app.db.database import engine
import os

# FastAPI 앱 생성
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Everyday Hiking Backend API with Firebase Authentication & JWT",
)

# ✅ CORS 설정 추가 (Next.js 개발 환경 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js 프론트엔드 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터베이스 연결 확인 (별도 engine 생성 없이 database.py의 engine 사용)
try:
    conn = engine.connect()
    print("데이터베이스 연결 성공!")
    conn.close()
except Exception as e:
    print("데이터베이스 연결 실패:", e)

# 기본 라우트
@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}

# FastAPI 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
