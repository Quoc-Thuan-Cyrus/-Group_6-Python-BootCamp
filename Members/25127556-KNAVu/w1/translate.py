def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Chuyển vị một ma trận biểu diễn bằng danh sách các danh sách (list of lists).

    Điểm khác biệt so với phiên bản C++:
    1. Quản lý kiểu dữ liệu và bộ nhớ: 
       Trong C++, ma trận sử dụng kiểu std::vector<std::vector<int>> cố định 
       và cần phải khởi tạo trước kích thước cho ma trận kết quả (cols x rows). 
       Trong Python, danh sách (list) là động, cho phép tạo và mở rộng ma trận 
       linh hoạt mà không cần khai báo kích thước ban đầu.
    
    2. Cú pháp Pythonic: 
       Thay vì dùng 2 vòng lặp for lồng nhau để gán thủ công từng phần tử 
       result[j][i] = matrix[i][j] như trong C++, Python cho phép tạo ma trận 
       chuyển vị ngắn gọn bằng cú pháp List Comprehension hoặc hàm zip(*matrix).
    """
    if not matrix:
        return []

    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]