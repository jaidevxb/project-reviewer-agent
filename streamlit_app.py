import streamlit as st
import os

from tools.repo_loader import load_repo
from agent.reviewer import review_repo
from agent.evaluator import evaluate
from agent.llm_summary import (
    generate_llm_summary,
    generate_resume_bullets,
)
from utils.report_exporter import export_markdown, export_pdf


# MUST be first Streamlit call
st.set_page_config(page_title="Autonomous Project Reviewer", layout="wide")


# ---- SIDEBAR ----
st.sidebar.title("🔑 API Configuration")

user_key = st.sidebar.text_input(
    "Enter your Groq API Key",
    type="password",
    help="Key is used only for this session."
)

if user_key:
    os.environ["GROQ_API_KEY"] = user_key

st.sidebar.markdown("---")

st.sidebar.markdown("""
### How to get a Groq API Key
1. Go to https://console.groq.com  
2. Sign in with Google  
3. Open **API Keys**  
4. Create a new key  
5. Paste it above  

✅ Free tier is enough for this app.
""")


# ---- MAIN UI ----
st.title("🧠 Autonomous Project Reviewer Agent")
st.write(
    "Analyze GitHub repositories and generate review reports, summaries, "
    "and resume-ready bullet points."
)

repo_url = st.text_input("🔗 Enter GitHub Repository URL")

if st.button("🚀 Review Project") and repo_url:
    with st.spinner("Cloning and analyzing repository..."):
        repo_path, files = load_repo(repo_url)
        report = review_repo(repo_path, files)
        result = evaluate(report)

    st.success("Analysis completed!")

    # ---- SCORE ----
    st.subheader("📊 Score Breakdown")
    col1, col2, col3 = st.columns(3)

    col1.metric("Code Quality", f"{result['scores']['code']} / 20")
    col2.metric("Documentation", f"{result['scores']['documentation']} / 10")
    col3.metric("Structure & Tests", f"{result['scores']['structure']} / 10")

    st.metric("🏁 Final Score", f"{result['final']} / 40")

    # ---- ISSUES ----
    st.subheader("📄 Documentation Issues")
    if result["report"]["documentation"]:
        for i in result["report"]["documentation"]:
            st.warning(i)
    else:
        st.success("No documentation issues found")

    st.subheader("🧩 Code Issues")
    if result["report"]["code"]:
        for i in result["report"]["code"]:
            st.error(i)
    else:
        st.success("No code issues found")

    st.subheader("🏗 Structure Issues")
    if result["report"]["structure"]:
        for i in result["report"]["structure"]:
            st.warning(i)
    else:
        st.success("No structure issues found")

    # ---- LLM SUMMARY ----
    st.subheader("🤖 LLM Summary & Recommendations")
    summary, recs = generate_llm_summary(result["report"])

    st.markdown("### Summary")
    st.markdown(summary)

    st.markdown("### Recommendations")
    st.markdown(recs)

    # ---- RESUME BULLETS FOR USER PROJECT ----
    st.subheader("🧾 Resume Bullets for This Project")
    st.caption("You can directly copy-paste these into your resume.")
    resume_bullets = generate_resume_bullets(result["report"])
    st.code(resume_bullets, language="text")

    # ---- EXPORT ----
    st.subheader("📥 Export Full Report")

    md_text = export_markdown(result, summary, recs)

    st.download_button(
        "⬇️ Download Markdown Report",
        md_text,
        file_name="report.md"
    )

    st.info(
        "PDF export is disabled on cloud deployments for stability. "
        "You can convert the Markdown report to PDF locally if needed."
    )


    # ---- EXAMPLE RESUME BULLETS (STATIC) ----
    st.markdown("---")
    st.subheader("📄 Example Resume Bullets (for THIS Tool)")

    st.caption(
        "Example of how *this* project can be described on a resume. "
        "This is just a reference."
    )

    st.code(
        """Autonomous Project Reviewer Agent
    Tech: Python, Agentic AI, LLMs (Groq), Streamlit

    • Built an autonomous agentic system that reviews GitHub repositories by analyzing code quality, documentation, and project structure.
    • Implemented deterministic static analysis to detect missing docstrings, oversized files, and structural issues.
    • Integrated LLM-based synthesis to generate human-readable project summaries and resume-ready bullet points.
    • Developed an interactive Streamlit application with score breakdowns and exportable Markdown/PDF reports.
    """,
        language="text"
    )
