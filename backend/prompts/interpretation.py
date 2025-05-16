# backend/prompts/interpretation.py
def get_interpretation_prompt(
    topic: str,
    industry: str,
    country: str,
    current_date: str,
    language: str,
    big_picture: str,
    mid_picture: str,
    small_picture: str,
    user_comment: str = ""
) -> str:
    return f"""
You are producing a strategic interpretation for a decision-maker in the {industry} sector in {country}, regarding the macroeconomic topic: {topic}.

This interpretation should reflect current realities as of {current_date}, based on the following multi-layered summaries:

# Input Summaries:
Big Picture:
{big_picture}

Mid Picture:
{mid_picture}

Small Picture:
{small_picture}

# Internal Analyst Comment (Optional):
"{user_comment if user_comment else '[None provided]'}"

# Instructions:
- The entire output must be written in {language}, which is selected by the user. Do not answer in English unless English is the selected language.
- Start by synthesizing the summaries into one cohesive interpretation.
- If any summary is based on fallback (historical analogues), acknowledge that explicitly.
- Focus on structural and behavioral implications for the sector today.
- Reflect the analyst comment respectfully, as a guiding context — not an override.
- End with a forward-looking projection covering the next 1–3 months.
- Do NOT merely summarize — interpret, connect, and project.
- Keep the tone professional and accessible for executive decision-making.
"""

