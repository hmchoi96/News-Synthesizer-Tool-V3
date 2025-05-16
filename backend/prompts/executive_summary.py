# backend/prompts/executive_summary.py

def get_executive_summary_prompt(
    topic: str,
    industry: str,
    country: str,
    language: str,
    current_date: str,
    big_picture: str,
    mid_picture: str,
    small_picture: str,
    interpretation: str
) -> str:
    return f"""
Generate a concise executive summary as of {current_date}, based on the following multi-level analysis of the macroeconomic topic '{topic}' and its impact on the {industry} sector in {country}.

# Input Summaries:
Big Picture:
{big_picture}

Mid Picture:
{mid_picture}

Small Picture:
{small_picture}

Interpretation:
{interpretation}

# Instructions:
- The entire output must be written in {language}, which is selected by the user. Do not answer in English unless English is the selected language.
- Summarize the key implications and directional insight from the full analysis.
- Limit to 3–5 sentences.
- Maintain a professional, report-ready tone.
- If any input was based on fallback (e.g., no recent data), briefly acknowledge that insight is inferred from past analogues.
- Do NOT include raw data, lengthy reasoning, or citations — only the most actionable and concise insight.
- Output must be suitable to appear at the top of a formal report or executive dashboard.
"""
