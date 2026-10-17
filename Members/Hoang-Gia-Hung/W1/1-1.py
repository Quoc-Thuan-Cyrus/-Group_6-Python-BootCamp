import statistics


def summary(scores: list[float]) -> dict:
    """W1-1: Grade summary.

    Returns {"min": ..., "max": ..., "mean": ..., "median": ...}.
    Rounds mean and median to 2 decimals.
    Raises ValueError on empty list.
    """
    if not scores:
        raise ValueError("Scores list cannot be empty.")

    sorted_scores = sorted(scores)
    return {
        "min": min(sorted_scores),
        "max": max(sorted_scores),
        "mean": round(statistics.mean(sorted_scores), 2),
        "median": round(statistics.median(sorted_scores), 2),
    }


if __name__ == "__main__":
    print(summary([7.5, 9, 6, 8]))
    # Expected: {'min': 6, 'max': 9, 'mean': 7.62, 'median': 7.75}
