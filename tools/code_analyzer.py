def analyze_code(code: str):
    issues = []

    if "TODO" in code:
        issues.append("Contains TODO comments")

    if code.count("\n") > 300:
        issues.append("File is too long, consider refactoring")

    if "def " in code and '"""' not in code:
        issues.append("Missing docstrings")

    return issues
