import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def _get_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None
    return Groq(api_key=api_key)


def generate_llm_summary(report):
    client = _get_client()
    if not client:
        return (
            "LLM summary not generated.",
            "Please provide a Groq API key in the sidebar."
        )

    prompt = f"""
You are a senior software engineer reviewing a software project.

Documentation issues:
{report['documentation']}

Code issues:
{report['code']}

Structure issues:
{report['structure']}

Give:
1. A concise overall project summary (5–6 lines)
2. Clear, actionable improvement recommendations
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


def generate_resume_bullets(report):
    client = _get_client()
    if not client:
        return "Please provide a Groq API key to generate resume bullets."

    prompt = f"""
You are a career coach writing resume bullets.

IMPORTANT:
- Do NOT claim that the code was modified or refactored.
- Describe what the PROJECT DOES, not changes made by the reviewer.
- Use past tense.
- Write bullets that a student can honestly put on their resume.

Project analysis:
Documentation issues:
{report['documentation']}

Code issues:
{report['code']}

Structure issues:
{report['structure']}

Write 3–4 concise, resume-ready bullet points describing THIS PROJECT.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()

