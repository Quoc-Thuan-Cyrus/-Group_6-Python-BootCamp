def _clean_text(text: str) -> list[str]:
    punctuations = [',', '.', '!', '?', ';', ':']
    cleaned_text = text.lower()
    for p in punctuations:
        cleaned_text = cleaned_text.replace(p, '')
    return cleaned_text.split()

def word_count(text: str) -> dict[str, int]:
    words = _clean_text(text)
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]