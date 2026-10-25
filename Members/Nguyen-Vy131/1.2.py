import re
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    cleaned_text = re.sub(r'[.,!?;:]', '', text.lower())
    words = cleaned_text.split()
    return dict(Counter(words))

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:k]