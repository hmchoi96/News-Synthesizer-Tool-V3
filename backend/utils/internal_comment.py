# backend/utils/internal_comment.py

import json
import os

FILE_PATH = "backend/config/internal_comment.json"

def save_internal_comment(text: str):
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    with open(FILE_PATH, "w") as f:
        json.dump({"comment": text}, f, ensure_ascii=False, indent=2)

def load_internal_comment() -> str:
    if not os.path.exists(FILE_PATH):
        return ""
    with open(FILE_PATH, "r") as f:
        return json.load(f).get("comment", "")
