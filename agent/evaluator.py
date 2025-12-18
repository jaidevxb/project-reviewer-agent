def evaluate(report):
    scores = {
        "code": 20,
        "documentation": 10,
        "structure": 10
    }

    for issue in report["code"]:
        scores["code"] -= 2

    for issue in report["documentation"]:
        scores["documentation"] -= 3

    for issue in report["structure"]:
        scores["structure"] -= 5

    final_score = sum(max(v, 0) for v in scores.values())

    return {
        "scores": scores,
        "final": final_score,
        "report": report
    }
