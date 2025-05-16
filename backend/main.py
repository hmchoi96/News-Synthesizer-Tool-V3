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
    allow_origins=["https://wiserbond-streamlit.onrender.com"],  # 프로덕션 시엔 도메인 제한하는 게 좋음
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
    internal_comment: str = ""
    user_forecast: str = ""
    user_analysis: str = ""
    is_pro: bool = False


# --- 메인 API 엔드포인트
@app.post("/generate_report")
def generate_report(data: ReportRequest):
    result = generate_full_report(
        topic=data.topic,
        industry=data.industry,
        country=data.country,
        language=data.language,
        internal_comment=data.internal_comment,
        user_forecast=data.user_forecast,
        user_analysis=data.user_analysis,
        is_pro=data.is_pro
    )
    return result

# ✅ 유저 피드백 입력 스키마
class FeedbackInput(BaseModel):
    email: str
    topic: str
    industry: str
    country: str
    user_forecast: str
    user_analysis: str

# ✅ 유저 피드백 저장 API
@app.post("/submit-feedback")
def submit_feedback(data: FeedbackInput):
    save_user_feedback(data)
    return {"status": "success", "message": "User feedback saved."}
