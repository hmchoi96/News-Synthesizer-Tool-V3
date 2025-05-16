# File: backend/utils/gpt_api.py
# Path: /backend/utils/gpt_api.py

import os, openai

# Render 배포 환경에서 설정한 OPENAI_API_KEY 사용
openai.api_key = os.environ["OPENAI_API_KEY"]

def call_gpt(prompt: str, model: str = "gpt-4o-mini", temperature: float = 0.3) -> str:
    """
    GPT 모델을 호출하여 텍스트를 생성합니다.

    Args:
        prompt (str): 모델에 전달할 프롬프트 문자열
        model (str): 사용할 모델 이름 (예: 'gpt-4o', 'gpt-4o-mini')
        temperature (float): 생성의 다양성 조절 파라미터

    Returns:
        str: 모델이 생성한 응답 텍스트
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content
