# File: backend/main.py
# Path: /backend/main.py

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .chains.generate_report import generate_full_report
from .models.feedback_model import FeedbackRequest
from .utils.save_user_feedback import save_user_feedback
from .utils.internal_comment import load_internal_comment, save_internal_comment

app = FastAPI()

# 1) 루트 엔드포인트 추가
@app.get("/")
def root():
    return {"status": "OK", "message": "Wiserbond API is running"}

# 2) CORS 설정: 개발 및 배포 환경에 맞춰 origin 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://wiserbond-streamlit.onrender.com",
        "https://wiserbond-synthesizerv3.onrender.com",
        "http://localhost:10000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 리포트 요청 형식 정의 ---
class ReportRequest(BaseModel):
    topic: str
    industry: str
    country: str
    language: str = "English"
    internal_comment: str = ""
    user_forecast: str = ""
    user_analysis: str = ""

@app.post("/generate")
def generate(report: ReportRequest):
    result = generate_full_report(
        topic=report.topic,
        industry=report.industry,
        country=report.country,
        language=report.language,
        user_comment=report.internal_comment,
        is_pro=False
    )
    return {"report": result}

# --- 내부 코멘트 로드/저장용 엔드포인트 추가 ---
@app.get("/load_internal_comment")
def get_internal_comment():
    comment = load_internal_comment()
    return {"comment": comment}

@app.post("/save_internal_comment")
def post_internal_comment(payload: dict = Body(...)):
    save_internal_comment(payload.get("comment", ""))
    return {"status": "success"}

# --- 사용자 피드백 저장 엔드포인트 ---
@app.post("/feedback")
def feedback(feedback: FeedbackRequest):
    save_user_feedback(feedback)
    return {"status": "saved"}
