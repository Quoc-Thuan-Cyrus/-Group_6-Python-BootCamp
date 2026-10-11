from collections import Counter


def word_count(text: str) -> dict[str, int]:
    # Loại bỏ các dấu câu: . , ! ? ; :
    punctuation = ".,!?;:"
    cleaned_text = "".join(ch for ch in text if ch not in punctuation)

    # Chuyển về chữ thường và tách từ
    words = cleaned_text.lower().split()
    return dict(Counter(words))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)

    # Sắp xếp: Tần suất giảm dần (-item[1]), Từ tăng dần theo bảng chữ cái (item[0])
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    return sorted_words[:k]


# Kiểm thử
if __name__ == "__main__":
    text = "Git is fun. Git is fast!"
    print(word_count(text))
    # Output: {'git': 2, 'is': 2, 'fun': 1, 'fast': 1}

    print(top_k(text, 2))
    # Output: [('git', 2), ('is', 2)]