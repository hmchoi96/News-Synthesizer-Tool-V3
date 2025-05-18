# File: backend/utils/gpt_api.py
import os
import openai

# 시스템 환경 변수에서 API 키 읽기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("환경 변수 OPENAI_API_KEY가 설정되지 않았습니다.")

# OpenAI 클라이언트에 키 등록
openai.api_key = OPENAI_API_KEY

def call_gpt(prompt: str, model: str = "gpt-4o") -> str:
    """
    GPT 모델에 프롬프트를 보내고 응답 텍스트를 반환합니다.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        # temperature, max_tokens 등 추가 옵션 가능
    )
    return response.choices[0].message.content
