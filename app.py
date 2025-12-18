import sys
import os
from agent.llm_summary import generate_llm_summary


from tools.repo_loader import load_repo
from agent.reviewer import review_repo
from agent.evaluator import evaluate


def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <github_repo_url>")
        sys.exit(1)

    repo_url = sys.argv[1]

    print("[+] Loading repository...")
    repo_path, files = load_repo(repo_url)

    print("[+] Planning review steps...")
    # planning is currently static (intentional)

    print("[+] Executing review...")
    report = review_repo(repo_path, files)

    print("[+] Evaluating project...")
    result = evaluate(report)

    print("\n--- PROJECT REVIEW REPORT ---\n")

    print(f"Code Quality: {result['scores']['code']} / 20")
    print(f"Documentation: {result['scores']['documentation']} / 10")
    print(f"Structure & Tests: {result['scores']['structure']} / 10")
    print(f"\nFINAL SCORE: {result['final']} / 40")

    print("\n## Documentation Issues")
    if result["report"]["documentation"]:
        for i in result["report"]["documentation"]:
            print("-", i)
    else:
        print("- None")

    print("\n## Code Issues")
    if result["report"]["code"]:
        for i in result["report"]["code"]:
            print("-", i)
    else:
        print("- None")

    print("\n## Structure Issues")
    if result["report"]["structure"]:
        for i in result["report"]["structure"]:
            print("-", i)
    else:
        print("- None")
    print("\n## LLM Summary")
    summary, recs = generate_llm_summary(result["report"])
    print(summary)

    print("\n## Recommendations")
    print(recs)



if __name__ == "__main__":
    main()
