def get_interpretation_prompt(
    topic: str,
    industry: str,
    country: str,
    current_date: str,
    language: str,
    big_picture: str,
    mid_picture: str,
    small_picture: str,
    internal_comment: str = "",
    user_forecast: str = "",
    user_analysis: str = "",
    is_pro: bool = False
) -> str:
    tone_instruction = (
        "Use technical, domain-specific language relevant to professionals in the selected industry. "
        "Avoid oversimplified explanations. Assume the reader is familiar with industry terminology."
        if is_pro else
        "Use clear, easy-to-understand language suitable for non-experts. Explain terms where necessary."
    )

    user_section = (
        f"User Analysis: \"{user_analysis}\"\nUser Forecast: \"{user_forecast}\""
        if user_forecast or user_analysis else
        "[No verified user forecasts available]"
    )

    return f"""
You are producing a strategic interpretation for a decision-maker in the {industry} sector in {country}, regarding the macroeconomic topic: {topic}.

This interpretation should reflect current realities as of {current_date}, based on the following multi-layered summaries:

{tone_instruction}

# Input Summaries:
Big Picture:
{big_picture}

Mid Picture:
{mid_picture}

Small Picture:
{small_picture}

# Internal Analyst Comment (Optional):
"{internal_comment if internal_comment else '[None provided]'}"

# Verified User Forecast & Analysis:
{user_section}

# Instructions:
- The entire output must be written in {language}, which is selected by the user. Do not answer in English unless English is the selected language.
- Start by synthesizing the summaries into one cohesive interpretation.
- If any summary is based on fallback (historical analogues), acknowledge that explicitly.
- Focus on structural and behavioral implications for the sector today.
- Reflect the analyst comment respectfully, as a guiding context — not an override.
- End with a forward-looking projection covering the next 1–3 months.
- If user-submitted forecasts or interpretations are present, include them at the end as a synthesized user perspective.
- Only include if they are relevant and logical; otherwise, ignore or flag as irrelevant.
- Do NOT merely summarize — interpret, connect, and project.
- Keep the tone professional and accessible for executive decision-making.
""".strip()
