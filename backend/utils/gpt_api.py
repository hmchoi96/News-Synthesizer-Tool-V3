# backend/utils/gpt_api.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def call_gpt(prompt: str, model: str = "gpt-4o", temperature: float = 0.7) -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT 호출 실패: {e}"
