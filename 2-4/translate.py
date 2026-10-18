from collections import Counter

# Task 1
def binary_search(arr: list[int], target: int) -> int:
    """Binary search on a sorted vector/list, returning the target index or -1 if not found.

    Differences from C++ version:
    1. Bounds and Length Handling: Python's len(arr) returns a signed integer, making bounds arithmetic safe even for an empty list[cite: 4].
    2. Integer Overflow: In Python, integers have arbitrary precision, so `(left + right) // 2` is inherently safe from integer overflow[cite: 4].
    3. Type Flexibility & Slicing: Python's dynamic typing allows duck-typing comparisons effortlessly[cite: 4].
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Task 2
def insertion_sort(arr: list) -> list:
    """
    Sorts a list in-place using the insertion sort algorithm and returns it.
    
    Difference from C++:
    In Python, we do not need to pass the size of the array as a separate 
    parameter because Python lists inherently know their own length[cite: 4].
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr


# Task 3
def transpose_matrix(matrix: list[list]) -> list[list]:
    """
    Transposes a 2D matrix (vector of vectors).
    
    Difference from C++:
    In C++, this requires initializing a new vector of vectors and using nested for-loops. 
    In Python, we can unpack the matrix using the * operator and zip it together to transpose 
    the rows and columns in a single, highly readable line.
    """
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


# Task 4
def sieve_of_eratosthenes(n: int) -> list[int]:
    """
    Sàng Eratosthenes tìm các số nguyên tố nhỏ hơn hoặc bằng n.
    
    Khác biệt so với C++:
    - Tạo mảng boolean `[True] * (n + 1)` nhanh hơn khởi tạo `std::vector<bool>`[cite: 4].
    """
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return [p for p in range(2, n + 1) if is_prime[p]]


# Task 5
def get_frequencies(elements: list) -> dict:
    """Đếm tần suất xuất hiện của các phần tử trong danh sách.

    Sự khác biệt so với C++ (std::map / std::unordered_map):
    - Trong C++, việc đếm tần suất đòi hỏi duyệt thủ công qua từng phần tử[cite: 4].
    - Trong Python, collections.Counter cho phép đếm toàn bộ tần suất ngay khi
      khởi tạo (one-liner) với độ phức tạp O(N)[cite: 4].
    """
    return dict(Counter(elements))


# Task 6
def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Merges two sorted arrays.
    
    Difference from C++:
    Instead of two-pointer manipulation or std::merge, Python's list unpacking 
    and built-in highly optimized Timsort algorithm allow merging and sorting concisely.
    """
    return sorted([*arr1, *arr2])


# Task 7
def reverse_words(s: str) -> str:
    """
    Reverses the words in a string.
    
    Difference from C++:
    C++ often requires std::stringstream or manual loop indexing to parse and reconstruct 
    the words. Python handles this natively by splitting the string into a list, slicing 
    it in reverse, and joining it back into a string.
    """
    return " ".join(s.split()[::-1])