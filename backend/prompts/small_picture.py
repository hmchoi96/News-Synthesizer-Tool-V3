# backend/prompts/small_picture.py

def get_small_picture_prompt(topic: str, industry: str, country: str, current_date: str, language: str) -> str:
    return f"""
Summarize any short-term developments (within the past 7–10 days from {current_date}) related to the macroeconomic topic '{topic}' and its potential or emerging effects on the {industry} sector in {country}.

Use only credible, factual news sources (e.g., Bloomberg, CNBC, Reuters). Avoid editorial, emotional, or political framing.

Your response must:
- The entire output must be written in {language}, which is selected by the user. Do not answer in English unless English is the selected language.
- Focus on time-sensitive events, policy announcements, corporate moves, or reactions clearly related to the topic.
- Reflect what has changed or emerged in the past few days.
- If there are no meaningful recent updates, fallback to a structurally similar past macro event and explain its relevance. Clearly state that this is a fallback case.
- Avoid repeating mid- or long-term projections already discussed in prior sections.
- Include the source name and publication date. Add a link if available.
- Do NOT include sentiment scoring or opinionated language.

Topic: {topic}
Industry: {industry}
Country: {country}
""".strip()
