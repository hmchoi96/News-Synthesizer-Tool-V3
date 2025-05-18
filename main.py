from fastapi import FastAPI, Body, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.chains.generate_report import generate_full_report
from backend.models.feedback_model import FeedbackRequest
from backend.utils.save_user_feedback import save_user_feedback
from backend.utils.internal_comment import load_internal_comment, save_internal_comment

app = FastAPI()

# CORS 설정
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

# 요청 데이터 스키마
class ReportRequest(BaseModel):
    topic: str
    industry: str
    country: str
    language: str = "English"
    internal_comment: str = ""
    user_forecast: str = ""
    user_analysis: str = ""
    is_pro: bool = False

# 보고서 생성 API
@app.post("/generate_report")
async def generate(report: ReportRequest, request: Request):
    debug_trace = []
    try:
        debug_trace.append("🚨 진입 성공")

        result = generate_full_report(
            topic=report.topic,
            industry=report.industry,
            country=report.country,
            language=report.language,
            internal_comment=report.internal_comment,
            user_forecast=report.user_forecast,
            user_analysis=report.user_analysis,
            is_pro=report.is_pro,
            debug_log=debug_trace  # 전달
        )

        debug_trace.append("✅ generate_full_report 종료")

        return {
            "report": result,
            "debug": debug_trace
        }
    except Exception as e:
        debug_trace.append(f"❌ 예외 발생: {str(e)}")
        return {
            "error": str(e),
            "debug": debug_trace,
            "detail": "❌ /generate_report 내부에서 예외 발생"
        }

# 내부 분석자 코멘트 로드/저장
@app.get("/load_internal_comment")
def get_internal_comment():
    return {"comment": load_internal_comment()}

@app.post("/save_internal_comment")
def post_internal_comment(payload: dict = Body(...)):
    save_internal_comment(payload.get("comment", ""))
    return {"status": "success"}

# 사용자 피드백 저장
@app.post("/submit-feedback")
def feedback(feedback: FeedbackRequest):
    fb = feedback.dict()
    from datetime import datetime
    fb["timestamp"] = datetime.utcnow().isoformat()
    save_user_feedback(fb)
    return {"status": "saved"}
