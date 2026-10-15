def word_count(text: str) -> dict[str, int]:
    punctuations = ".,!?;:"
    for ch in punctuations:
        text = text.replace(ch, " ")
    
    words = text.lower().split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]