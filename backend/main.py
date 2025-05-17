# File: backend/main.py
# Path: /backend/main.py

from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import traceback

from .chains.generate_report import generate_full_report
from .models.feedback_model import FeedbackRequest
from .utils.save_user_feedback import save_user_feedback
from .utils.internal_comment import load_internal_comment, save_internal_comment

app = FastAPI()

# 1) 헬스체크용 엔드포인트
@app.get("/")
def root():
    return {"status": "OK", "message": "Wiserbond API is running"}

# 2) CORS 설정: 로컬(8501,10000)과 배포 도메인 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",
        "http://localhost:10000",
        "https://wiserbond-streamlit.onrender.com",
        "https://wiserbond-synthesizerv3.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ReportRequest 스키마
class ReportRequest(BaseModel):
    topic: str
    industry: str
    country: str
    language: str = "English"
    internal_comment: str = ""
    user_forecast: str = ""
    user_analysis: str = ""
    is_pro: bool = False


# 3) 리포트 생성 엔드포인트 (에러 로깅 포함)
@app.post("/generate_report")
def generate(report: ReportRequest):
    try:
        result = generate_full_report(
            topic=report.topic,
            industry=report.industry,
            country=report.country,
            language=report.language,
            internal_comment=report.internal_comment,
            is_pro=False
        )
        return {"report": result}
    except Exception as e:
        # 콘솔에 스택트레이스 찍기
        traceback.print_exc()
        # 클라이언트에 상태 코드 500과 상세 메시지 전달
        raise HTTPException(status_code=500, detail=f"Error generating report: {e}")

# 4) 내부 코멘트 로드/저장
@app.get("/load_internal_comment")
def get_internal_comment():
    return {"comment": load_internal_comment()}

@app.post("/save_internal_comment")
def post_internal_comment(payload: dict = Body(...)):
    save_internal_comment(payload.get("comment", ""))
    return {"status": "success"}

# 5) 사용자 피드백 저장
@app.post("/feedback")
def feedback(feedback: FeedbackRequest):
    save_user_feedback(feedback)
    return {"status": "saved"}
