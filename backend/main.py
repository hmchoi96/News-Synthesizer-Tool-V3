# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .chains.generate_report import generate_full_report
# ✅ 새로 추가
from .models.feedback_model import FeedbackRequest
from .utils.save_user_feedback import save_user_feedback
app = FastAPI()


# --- (선택) CORS 설정: 프론트에서 호출 가능하도록 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션 시엔 도메인 제한하는 게 좋음
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 리포트 요청 형식 정의
class ReportRequest(BaseModel):
    topic: str
    industry: str
    country: str
    language: str = "English"
    user_comment: str = ""

# --- 메인 API 엔드포인트
@app.post("/generate_report")
def generate_report(data: ReportRequest):
    result = generate_full_report(
        topic=data.topic,
        industry=data.industry,
        country=data.country,
        language=data.language,
        user_comment=data.user_comment
    )
    return result

# --- CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 리포트 요청 형식
class ReportRequest(BaseModel):
    topic: str
    industry: str
    country: str
    language: str = "English"
    user_comment: str = ""

# --- 리포트 생성 API
@app.post("/generate_report")
def generate_report(data: ReportRequest):
    result = generate_full_report(
        topic=data.topic,
        industry=data.industry,
        country=data.country,
        language=data.language,
        user_comment=data.user_comment
    )
    return result

# ✅ 유저 피드백 저장 API
@app.post("/submit-feedback")
def submit_feedback(data: FeedbackRequest):
    save_user_feedback(data.dict())
    return {"status": "success"}

