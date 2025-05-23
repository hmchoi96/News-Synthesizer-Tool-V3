def get_mid_picture_prompt(topic: str, industry: str, country: str, current_date: str, language: str,is_pro: bool = False
    ) -> str:
    tone_instruction = (
        "Use technical, domain-specific language relevant to professionals in the selected industry. "
        "Avoid oversimplified explanations. Assume the reader is familiar with industry terminology."
        if is_pro else
        "Use clear, easy-to-understand language suitable for non-experts. Explain terms where necessary."
    )

    return f"""
Analyze how the macroeconomic topic '{topic}' has affected the {industry} sector in {country} over the past quarter or month.

Use reliable sources such as:
- Consulting firms (Deloitte, BCG, McKinsey, Bain& etc.)
- Bank and industry reports in {country}
- Trade association publications
- Economic think tanks

Your response must:
- The entire output must be written in {language}, which is selected by the user. Do not answer in English unless English is the selected language.
- Prioritize analyst outlooks and reports from 2024 Q4 or 2025 Q1 when available.
- Reflect the economic and industry environment as of {current_date}.
- Focus on business responses, financial impacts, operational adjustments, or investor reactions.
- Summarize recent trends, such as: “Policy shift → cost increase → hiring slowdown”, if relevant.
- Include at least one named source (URL if available).
- If no recent data exists, fallback to a structurally similar quarter and clearly indicate this fallback.
- Do not include sentiment analysis or subjective emotion-related language.

Topic: {topic}
Industry: {industry}
Country: {country}
""".strip()
