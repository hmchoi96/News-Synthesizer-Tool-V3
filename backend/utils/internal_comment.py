# File: backend/utils/internal_comment.py
import os
from datetime import datetime
import json

# backend/data/ 폴더 안에 JSON 저장
FILE_PATH = "backend/data/internal_comment.json"

# 폴더가 없으면 자동 생성
os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

def load_internal_comment() -> dict:
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_internal_comment(comment: str):
    data = {
        "comment": comment,
        "timestamp": datetime.utcnow().isoformat()
    }
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
