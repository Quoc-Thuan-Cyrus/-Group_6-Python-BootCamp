import statistics


def summary(scores: list[float]) -> dict:
    """Summarize a list of student exam scores.

    Computes the minimum, maximum, mean (rounded to 2 decimal places),
    and median (rounded to 2 decimal places).
    Raises ValueError if scores list is empty.
    """
    if not scores:
        raise ValueError("The scores list cannot be empty.")

    sorted_scores = sorted(scores)
    min_score = min(sorted_scores)
    max_score = max(sorted_scores)
    mean_score = round(statistics.mean(sorted_scores), 2)
    median_score = round(statistics.median(sorted_scores), 2)

    return {
        "min": min_score,
        "max": max_score,
        "mean": mean_score,
        "median": median_score,
    }


if __name__ == "__main__":
    test_scores = [7.5, 9.0, 6.0, 8.0]
    print("Scores:", test_scores)
    print("Summary:", summary(test_scores))
