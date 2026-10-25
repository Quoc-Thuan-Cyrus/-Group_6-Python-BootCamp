from collections import Counter


def count_frequencies(elements: list) -> dict:
    """Đếm tần suất xuất hiện của các phần tử trong danh sách.

    Sự khác biệt so với C++ (std::map / std::unordered_map):
    - Trong C++, việc đếm tần suất đòi hỏi duyệt thủ công qua từng phần tử
      và chèn/cập nhật vào std::map (cây đỏ-đen, O(log N)) hoặc
      std::unordered_map (bảng băm, O(1) trung bình) thông qua toán tử []
      hoặc find()/insert().
    - Trong Python, collections.Counter cho phép đếm toàn bộ tần suất ngay khi
      khởi tạo (one-liner) với độ phức tạp O(N). Nếu dùng dict thông thường,
      phương thức .get(key, 0) cũng hỗ trợ lấy giá trị mặc định ngắn gọn và an toàn.
    """
    return dict(Counter(elements))


if __name__ == "__main__":
    sample_data = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = count_frequencies(sample_data)
    print("Ket qua:", result)
