from tools.file_reader import read_file
from tools.code_analyzer import analyze_code

def review_repo(base_path, file_paths):
    report = {
        "documentation": [],
        "code": [],
        "structure": []
    }

    # README analysis
    readme = next((f for f in file_paths if "readme" in f.lower()), None)
    if readme:
        content = read_file(base_path, readme)
        if content:
            if "install" not in content.lower():
                report["documentation"].append("README missing installation instructions")
            if "usage" not in content.lower():
                report["documentation"].append("README missing usage section")
    else:
        report["documentation"].append("README not found")

    # Tests
    if not any("test" in f.lower() for f in file_paths):
        report["structure"].append("No test files found")

    # Code checks
    for f in file_paths:
        if f.endswith(".py"):
            content = read_file(base_path, f)
            if content:
                issues = analyze_code(content)
                if issues:
                    for i in issues:
                        report["code"].append(f"{f}: {i}")

    return report
