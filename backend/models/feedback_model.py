# backend/models/feedback_model.py

from pydantic import BaseModel

class FeedbackRequest(BaseModel):
    email: str
    topic: str
    industry: str
    country: str
    user_analysis: str
    user_forecast: str
