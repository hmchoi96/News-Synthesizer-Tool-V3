from datetime import datetime

def generate_full_report(
    topic,
    industry,
    country,
    language="English",
    internal_comment="",
    user_forecast="",
    user_analysis="",
    is_pro=False,
    debug_log=None
):
    from backend.prompts.big_picture import get_big_picture_prompt
    from backend.prompts.mid_picture import get_mid_picture_prompt
    from backend.prompts.small_picture import get_small_picture_prompt
    from backend.prompts.interpretation import get_interpretation_prompt
    from backend.prompts.executive_summary import get_executive_summary_prompt
    from backend.utils.gpt_api import call_gpt
    from backend.utils.internal_comment import load_internal_comment

    if debug_log is None:
        debug_log = []

    debug_log.append("📌 generate_full_report 시작")

    final_comment = internal_comment if internal_comment else load_internal_comment()
    current_date = datetime.today().strftime("%Y-%m-%d")

    # 1. Big Picture
    debug_log.append("🧠 1단계: big_prompt 생성")
    big_prompt = get_big_picture_prompt(topic, industry, country, current_date, language, is_pro)
    debug_log.append("🧠 1단계: big_prompt 완료 → GPT 호출")
    big_result = call_gpt(prompt=big_prompt, model="gpt-4")
    debug_log.append("✅ 1단계: big GPT 결과 수신")

    # 2. Mid Picture
    debug_log.append("🧠 2단계: mid_prompt 생성")
    mid_prompt = get_mid_picture_prompt(topic, industry, country, current_date, language, is_pro)
    mid_result = call_gpt(prompt=mid_prompt, model="gpt-4")
    debug_log.append("✅ 2단계: mid GPT 결과 수신")

    # 3. Small Picture
    debug_log.append("🧠 3단계: small_prompt 생성")
    small_prompt = get_small_picture_prompt(topic, industry, country, current_date, language, is_pro)
    small_result = call_gpt(prompt=small_prompt, model="gpt-4")
    debug_log.append("✅ 3단계: small GPT 결과 수신")

    # 4. Interpretation
    debug_log.append("🧠 4단계: interpretation_prompt 생성")
    interpretation_prompt = get_interpretation_prompt(
        topic=topic,
        industry=industry,
        country=country,
        current_date=current_date,
        big_picture=big_result,
        mid_picture=mid_result,
        small_picture=small_result,
        internal_comment=final_comment,
        user_forecast=user_forecast,
        user_analysis=user_analysis,
        language=language,
        is_pro=is_pro
    )
    interpretation_result = call_gpt(prompt=interpretation_prompt, model="gpt-4")
    debug_log.append("✅ 4단계: interpretation GPT 결과 수신")

    # 5. Executive Summary
    debug_log.append("🧠 5단계: executive_summary_prompt 생성")
    exec_prompt = get_executive_summary_prompt(
        topic=topic,
        industry=industry,
        country=country,
        current_date=current_date,
        big_picture=big_result,
        mid_picture=mid_result,
        small_picture=small_result,
        interpretation=interpretation_result,
        language=language,
        is_pro=is_pro
    )
    executive_result = call_gpt(prompt=exec_prompt, model="gpt-4")
    debug_log.append("✅ 5단계: executive_summary GPT 결과 수신")

    return {
        "executive_summary": executive_result,
        "big_picture": big_result,
        "mid_picture": mid_result,
        "small_picture": small_result,
        "interpretation": interpretation_result,
    }
