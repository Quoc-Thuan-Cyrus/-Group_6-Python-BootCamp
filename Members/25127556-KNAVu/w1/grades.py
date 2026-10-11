import statistics

def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("The scores list cannot be empty.")
    
    sorted_scores = sorted(scores)
    min_val = min(sorted_scores)
    max_val = max(sorted_scores)
    mean_val = round(statistics.mean(sorted_scores), 2)
    median_val = round(statistics.median(sorted_scores), 2)
    
    return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val
    }
