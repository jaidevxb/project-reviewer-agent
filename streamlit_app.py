import streamlit as st

from tools.repo_loader import load_repo
from agent.reviewer import review_repo
from agent.evaluator import evaluate
from agent.llm_summary import generate_llm_summary
from utils.report_exporter import export_markdown, export_pdf


st.set_page_config(page_title="Autonomous Project Reviewer", layout="wide")

st.title("🧠 Autonomous Project Reviewer Agent")
st.write("Analyze GitHub repositories using agentic AI + rule-based analysis")

repo_url = st.text_input("🔗 Enter GitHub Repository URL")

if st.button("🚀 Review Project") and repo_url:
    with st.spinner("Cloning and analyzing repository..."):
        repo_path, files = load_repo(repo_url)
        report = review_repo(repo_path, files)
        result = evaluate(report)

    st.success("Analysis completed!")

    # ---- SCORE SECTION ----
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
    st.write(summary)

    st.markdown("### Recommendations")
    st.write(recs)

    # ---- EXPORT SECTION ----
    st.subheader("📥 Export Report")

    md_text = export_markdown(result, summary, recs)
    export_pdf(md_text)

    st.download_button(
        "⬇️ Download Markdown Report",
        md_text,
        file_name="report.md"
    )

    with open("report.pdf", "rb") as f:
        st.download_button(
            "⬇️ Download PDF Report",
            f,
            file_name="report.pdf"
        )
