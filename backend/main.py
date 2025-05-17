# File: backend/main.py
# Path: /backend/main.py

from fastapi import FastAPI, Body, HTTPException, Request
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

# 2) CORS 설정
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

# 3) 요청 데이터 스키마
class ReportRequest(BaseModel):
    topic: str
    industry: str
    country: str
    language: str = "English"
    internal_comment: str = ""
    user_forecast: str = ""
    user_analysis: str = ""
    is_pro: bool = False

# 4) 보고서 생성 API
@app.post("/generate_report")
async def generate(report: ReportRequest, request: Request):
    try:
        print("✅ /generate_report 요청 도착")
        print("📦 요청 body (raw):", await request.body())
        print("📌 파싱된 ReportRequest:", report.dict())

        result = generate_full_report(
            topic=report.topic,
            industry=report.industry,
            country=report.country,
            language=report.language,
            internal_comment=report.internal_comment,
            user_forecast=report.user_forecast,
            user_analysis=report.user_analysis,
            is_pro=report.is_pro
        )

        print("✅ 보고서 생성 완료")
        return {"report": result}
    except Exception as e:
        print("❌ 예외 발생:")
        traceback.print_exc()
        print("🔍 예외 내용:", str(e))
        raise HTTPException(status_code=500, detail=f"Error generating report: {e}")

# 5) 내부 분석자 코멘트 로드/저장
@app.get("/load_internal_comment")
def get_internal_comment():
    return {"comment": load_internal_comment()}

@app.post("/save_internal_comment")
def post_internal_comment(payload: dict = Body(...)):
    save_internal_comment(payload.get("comment", ""))
    return {"status": "success"}

# 6) 사용자 피드백 저장
@app.post("/submit-feedback")
def feedback(feedback: FeedbackRequest):
    save_user_feedback(feedback)
    return {"status": "saved"}
