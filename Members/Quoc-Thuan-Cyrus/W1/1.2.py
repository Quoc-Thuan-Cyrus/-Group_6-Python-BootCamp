def word_count(text: str) -> dict[str, int]:
    punctuations = ".,!?;: "
    for ch in punctuations:
        text = text.replace(ch, " ")
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1 
    return counts
