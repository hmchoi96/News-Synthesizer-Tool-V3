# backend/utils/save_user_feedback.py
import json
from datetime import datetime
from pathlib import Path

def save_user_feedback(data, filename="user_feedback.json"):
    filepath = Path(filename)

    # 기존 데이터 로드
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    # 타임스탬프 추가
    data["timestamp"] = datetime.utcnow().isoformat()
    existing_data.append(data)

    # 저장
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, indent=2, ensure_ascii=False)
