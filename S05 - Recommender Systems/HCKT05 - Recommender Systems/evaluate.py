"""Evaluation script for the BGG Recommender System Hackathon."""
import json
import sys


def average_precision_at_k(recommended: list, relevant: set, k: int = 10) -> float:
    """Compute AP@k for a single user."""
    if not relevant:
        return 0.0
    recommended = recommended[:k]
    hits = 0
    score = 0.0
    for i, item in enumerate(recommended):
        if item in relevant:
            hits += 1
            score += hits / (i + 1)
    return score / min(len(relevant), k)


def mean_average_precision_at_k(submission: dict, ground_truth: dict, k: int = 10) -> float:
    """Compute mAP@k across all users."""
    scores = []
    for user_id, relevant_items in ground_truth.items():
        recommended = submission.get(user_id, [])
        ap = average_precision_at_k(recommended, set(relevant_items), k)
        scores.append(ap)
    return sum(scores) / len(scores) if scores else 0.0


def validate_submission(submission: dict, ground_truth: dict, k: int = 10):
    """Check submission format and print warnings."""
    missing = set(ground_truth.keys()) - set(submission.keys())
    extra = set(submission.keys()) - set(ground_truth.keys())
    wrong_length = {u: len(v) for u, v in submission.items() if len(v) != k}

    if missing:
        print(f"WARNING: {len(missing)} users missing from submission")
    if extra:
        print(f"WARNING: {len(extra)} extra users in submission (will be ignored)")
    if wrong_length:
        print(f"WARNING: {len(wrong_length)} users don't have exactly {k} recommendations")

    return len(missing) == 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python evaluate.py ground_truth.json submission.json")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        ground_truth = json.load(f)
    with open(sys.argv[2]) as f:
        submission = json.load(f)

    validate_submission(submission, ground_truth)
    score = mean_average_precision_at_k(submission, ground_truth)
    print(f"\nmAP@10: {score:.6f}")
