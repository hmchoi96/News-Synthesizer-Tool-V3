# File: backend/utils/gpt_api.py
# Path: /backend/utils/gpt_api.py

import os
import openai
from dotenv import load_dotenv

# Render 배포 시에는 이미 환경변수에 OPENAI_API_KEY가 설정되어 있으므로
# 별도의 .env 파일이 없어도 load_dotenv()를 호출해도 무방
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_gpt(prompt: str, model: str = "gpt-4o-mini", temperature: float = 0.3):
    """
    GPT 모델을 호출하여 텍스트를 생성합니다.

    :param prompt: 모델에 전달할 프롬프트 문자열
    :param model: 사용할 모델 이름 (예: 'gpt-4o', 'gpt-4o-mini')
    :param temperature: 생성의 다양성 조절 파라미터
    :return: 모델이 생성한 응답 텍스트
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content
