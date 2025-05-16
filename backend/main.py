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

# Health‑check endpoint at “/” to avoid 404 on HEAD/GET /
@app.get("/")
def root():
    return {"status": "OK", "message": "Wiserbond API is running"}

# CORS 설정: 로컬 테스트 및 실제 배포 도메인 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:10000",
        "https://wiserbond-streamlit.onrender.com",
        "https://wiserbond-synthesizerv3.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body schema for report generation
class ReportRequest(BaseModel):
    topic: str
    industry: str
    country: str
    language: str = "English"
    internal_comment: str = ""
    user_forecast: str = ""
    user_analysis: str = ""

# 리포트 생성 엔드포인트
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

# 내부 코멘트 로드용 엔드포인트
@app.get("/load_internal_comment")
def get_internal_comment():
    return {"comment": load_internal_comment()}

# 내부 코멘트 저장용 엔드포인트
@app.post("/save_internal_comment")
def post_internal_comment(payload: dict = Body(...)):
    save_internal_comment(payload.get("comment", ""))
    return {"status": "success"}

# 사용자 피드백 저장용 엔드포인트
@app.post("/feedback")
def feedback(feedback: FeedbackRequest):
    save_user_feedback(feedback)
    return {"status": "saved"}
