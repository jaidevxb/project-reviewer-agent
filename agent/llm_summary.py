import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def generate_llm_summary(report):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return (
            "LLM summary not generated.",
            "Please provide a valid Groq API key in the sidebar."
        )

    client = Groq(api_key=api_key)

    prompt = f"""
You are a senior software engineer reviewing a project.

Documentation issues:
{report['documentation']}

Code issues:
{report['code']}

Structure issues:
{report['structure']}

Give:
1. A concise overall summary (5–6 lines)
2. Clear, actionable recommendations
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    text = response.choices[0].message.content

    if "Recommendations" in text:
        summary, recs = text.split("Recommendations", 1)
    else:
        summary, recs = text, ""

    return summary.strip(), recs.strip()
