
# 🧠 Autonomous Project Reviewer Agent

A compact, explainable agent that reviews GitHub repositories using deterministic static analysis plus LLM-based synthesis to generate a human-readable summary and actionable recommendations.

---

## 🚀 Key Features

- Repository cloning and safe file enumeration
- Deterministic checks for missing docstrings, TODOs, and oversized files
- Project scoring for Code Quality, Documentation, and Structure & Tests
- LLM-based synthesis (Groq) for final summary and actionable recommendations
- CLI and Streamlit UI
- Report export to Markdown / PDF
- Modular, explainable architecture

---

## 🏗 How it works

1. Clone repository and enumerate files (skips ignored folders).
2. Read whitelisted files (safety checks: extensions and size limits).
3. Run deterministic static checks and collect issues.
4. Score the project across defined categories.
5. Generate a concise LLM summary and recommendations.
6. Present results via CLI or Streamlit and allow export to Markdown/PDF.

> Deterministic checks are used for reliability; the LLM (Groq) is used only for concise synthesis and recommendations.

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** (UI)
- **Groq LLM API**
- **python-dotenv**
- **GitPython**

---

## 📁 Project Structure

```text
project-reviewer-agent/
├── agent/
│   ├── reviewer.py      # Core review logic
│   ├── evaluator.py     # Scoring and evaluation
│   └── llm_summary.py   # LLM-based summary generation
├── tools/
│   ├── repo_loader.py   # GitHub repo cloning
│   ├── file_reader.py   # Safe file reading
│   └── code_analyzer.py # Static code checks
├── streamlit_app.py     # Streamlit UI
├── app.py               # CLI entry point
├── requirements.txt
├── .env                 # Environment variables (not committed)
├── .gitignore
└── README.md
```

## 🔐 Environment Setup

Create a `.env` file in the project root:

GROQ_API_KEY=your_groq_api_key_here

> ⚠️ Do NOT commit the `.env` file to GitHub.

---

## ▶️ How to Run (CLI)

```bash
python app.py https://github.com/username/repository
```

## ▶️ How to Run (Streamlit UI)

```bash
streamlit run streamlit_app.py
```

Paste a GitHub repository URL and click Review Project.

📊 Sample Output

```text
Code Quality: 12 / 20
Documentation: 8 / 10
Structure & Tests: 6 / 10

Final Score: 26 / 40
```

Includes:

Categorized issues (Documentation, Code, Structure)

LLM-generated project summary

Clear, actionable recommendations

## 💡 Design Philosophy

- Prefer deterministic checks for core verification
- Use LLMs only for concise synthesis and human-facing recommendations

Build agentic systems that are:

- Reliable
- Explainable
- Practical
- Resume-worthy

## 🚧 Roadmap / Future Improvements

- Export reports as Markdown / PDF (improved formatting)
- Compare multiple repositories / benchmarking
- Configurable scoring weights
- GitHub Action integration for automated reviews

👤 Author
Jaidev
Aspiring Data Scientist & AI Engineer
Building agentic systems and learning in public 🚀


---


