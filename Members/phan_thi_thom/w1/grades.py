def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Danh sách điểm rỗng.")
    
    n = len(scores)
    min_score = min(scores)
    max_score = max(scores)
    mean_score = round(sum(scores) / n, 2)
    
    sorted_scores = sorted(scores)
    mid = n // 2
    if n % 2 == 1:
        median_score = sorted_scores[mid]
    else:
        median_score = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
        
    median_score = round(median_score, 2)
    
    return {
        "min": min_score,
        "max": max_score,
        "mean": mean_score,
        "median": median_score
    }