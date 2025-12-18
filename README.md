
# 🧠 Autonomous Project Reviewer Agent

An agentic AI system that automatically reviews GitHub repositories by analyzing
code quality, documentation, and project structure, and then generates a
human-readable summary and actionable recommendations using a Large Language Model (LLM).

This project combines **deterministic static analysis** with **LLM-based synthesis**
to produce reliable, explainable, and practical project reviews.

---

## 🚀 Features

- 🔍 Clones and analyzes GitHub repositories
- 📊 Scores projects across multiple dimensions:
  - Code Quality
  - Documentation
  - Structure & Testing
- 🧠 Detects issues such as:
  - Missing docstrings
  - Oversized / unrefactored files
  - Missing tests
  - Incomplete README sections
- 🤖 Generates:
  - High-level project summary
  - Actionable improvement recommendations
- 🖥 Interactive Streamlit UI for easy usage
- 🧩 Clean, modular, agent-style architecture

---

## 🏗 Architecture Overview

GitHub Repo
↓
Rule-based Static Analysis
↓
Scoring Engine
↓
LLM-based Summary & Recommendations
↓
Streamlit UI / CLI Output

- **Deterministic tools** handle correctness and scoring  
- **LLM (Groq)** is used only for synthesis and reasoning  
- This design minimizes hallucination and improves reliability

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** (UI)
- **Groq LLM API**
- **python-dotenv**
- **GitPython**

---

## 📁 Project Structure

project-reviewer-agent/
│
├── agent/
│ ├── reviewer.py # Core review logic
│ ├── evaluator.py # Scoring and evaluation
│ └── llm_summary.py # LLM-based summary generation
│
├── tools/
│ ├── repo_loader.py # GitHub repo cloning
│ ├── file_reader.py # Safe file reading
│ └── code_analyzer.py # Static code checks
│
├── streamlit_app.py # Streamlit UI
├── app.py # CLI entry point
├── requirements.txt
├── .env # Environment variables (not committed)
├── .gitignore
└── README.md

---

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

💡 Design Philosophy
Avoid overusing LLMs where deterministic rules are sufficient

Use LLMs only for high-level synthesis and reasoning

Build agentic systems that are:

Reliable

Explainable

Practical

Resume-worthy

🚧 Future Improvements
Export reports as Markdown / PDF

Compare multiple repositories

Configurable scoring weights

GitHub Action integration for automated reviews

👤 Author
Jaidev
Aspiring Data Scientist & AI Engineer
Building agentic systems and learning in public 🚀


---


