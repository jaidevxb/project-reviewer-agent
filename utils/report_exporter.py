from fpdf import FPDF
import markdown

def export_markdown(result, summary, recs):
    md = f"""
# Project Review Report

## Scores
- Code Quality: {result['scores']['code']} / 20
- Documentation: {result['scores']['documentation']} / 10
- Structure & Tests: {result['scores']['structure']} / 10
- **Final Score:** {result['final']} / 40

## Documentation Issues
{chr(10).join('- ' + i for i in result['report']['documentation']) or '- None'}

## Code Issues
{chr(10).join('- ' + i for i in result['report']['code']) or '- None'}

## Structure Issues
{chr(10).join('- ' + i for i in result['report']['structure']) or '- None'}

## LLM Summary
{summary}

## Recommendations
{recs}
"""
    with open("report.md", "w", encoding="utf-8") as f:
        f.write(md)

    return md


def export_pdf(markdown_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=10)

    text = markdown_text.replace("#", "").replace("*", "")
    for line in text.split("\n"):
        pdf.multi_cell(0, 6, line)

    pdf.output("report.pdf")
