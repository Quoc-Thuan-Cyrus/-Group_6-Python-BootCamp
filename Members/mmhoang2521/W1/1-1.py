import statistics


def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Danh sách điểm không được để rỗng.")

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(statistics.mean(scores), 2),
        "median": round(statistics.median(scores), 2),
    }


# Kiểm thử
if __name__ == "__main__":
    print(summary([7.5, 9, 6, 8]))
    # Output: {'min': 6, 'max': 9, 'mean': 7.62, 'median': 7.75}