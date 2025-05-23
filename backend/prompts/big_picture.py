def get_big_picture_prompt(topic: str, industry: str, country: str, current_date: str, language: str, is_pro: bool = False) -> str:
    tone_instruction = (
        "Use technical, domain-specific language relevant to professionals in the selected industry. "
        "Avoid oversimplified explanations. Assume the reader is familiar with industry terminology."
        if is_pro else
        "Use clear, easy-to-understand language suitable for non-experts. Explain terms where necessary."
    )
    return f"""
Analyze how the selected macroeconomic topic or event affects the {industry} sector in {country} from a long-term institutional perspective.

Use only high-credibility sources such as:
- Central banks in {country} (e.g., Bank of Canada, FED, ECB)
- National banks in {country} (e.g., TD, Scotiabank, BMO)
- International institutions (IMF, OECD)
- Government statistical agencies in {country} (e.g., Statistics Canada)

Your response must:
- The entire output must be written in {language}, which is selected by the user. Do not answer in English unless English is the selected language.
- Reflect the most current economic outlooks and institutional analysis, prioritizing reports from 2024 Q4 or 2025 Q1 when available.
- Base your assessment on information valid as of {current_date}.
- Focus on the structural impact of the topic on the industry in {country}.
- Use clear, logical cause-effect phrasing (e.g., “Tariff → cost rise → margin pressure”), if helpful.
- Include at least one cited institution or source by name (URL if available).
- If no recent institutional data is available, fallback to historically similar macroeconomic events — and clearly state that this is a fallback case.
- Do NOT use sentiment scoring or subjective opinions.

Topic: {topic}
Industry: {industry}
Country: {country}
""".strip()
