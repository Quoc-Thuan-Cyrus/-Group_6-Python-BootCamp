from collections import Counter


def word_count(text: str) -> dict[str, int]:
    """W1-2: Count word frequencies in text (lower-case, ignore punctuation .,!?;:)."""
    punctuations = ".,!?;:"
    for ch in punctuations:
        text = text.replace(ch, " ")
    words = text.lower().split()
    return dict(Counter(words))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """W1-2: Return top-k words sorted by count descending, then alphabetically."""
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]


if __name__ == "__main__":
    sample_text = "Git is fun. Git is fast!"
    print("word_count:", word_count(sample_text))
    print("top_k:", top_k(sample_text, 2))
    # Expected: [('git', 2), ('is', 2)]
