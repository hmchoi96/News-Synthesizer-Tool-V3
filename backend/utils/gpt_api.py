# File: backend/utils/gpt_api.py
import os
import openai

# 시스템 환경 변수에서 API 키 읽기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("환경 변수 OPENAI_API_KEY가 설정되지 않았습니다.")

# OpenAI 클라이언트에 키 등록
openai.api_key = OPENAI_API_KEY

def call_gpt(prompt: str, model: str = "gpt-4") -> str:
    """
    GPT 모델에 프롬프트를 보내고 응답 텍스트를 반환합니다.
    예외 발생 시 로그를 출력하고 예외를 다시 raise 합니다.
    """
    try:
        print("🧠 GPT 호출 시작")
        print(f"📌 사용 모델: {model}")
        print("📨 프롬프트 일부:", prompt[:200], "...")

        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        print("✅ GPT 응답 수신 완료")

        # 응답 구조 확인
        if "choices" in response and len(response["choices"]) > 0:
            content = response["choices"][0]["message"]["content"]
            print("🧾 응답 요약:", content[:150], "...")
            return content
        else:
            print("⚠️ GPT 응답 구조가 예상과 다릅니다:", response)
            raise ValueError("Unexpected response structure from GPT")

    except Exception as e:
        print("❌ GPT 호출 중 예외 발생:", str(e))
        raise
