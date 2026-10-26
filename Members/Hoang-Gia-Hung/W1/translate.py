def binary_search(arr: list[int], target: int) -> int:
    """Binary search on a sorted vector/list, returning the target index or -1 if not found.

    Parameters:
        arr (list[int]): Sorted list of integers.
        target (int): Value to search for.

    Returns:
        int: Index of target in arr, or -1 if target is not present.

    Differences from C++ version:
    1. Bounds and Length Handling:
       In C++ (`std::vector<int>& v`), the size is queried via `v.size()`, which returns
       an unsigned type (`size_t`), requiring careful subtraction (`v.size() - 1`) to avoid
       unsigned underflow when the vector is empty. In Python, `len(arr)` returns a signed integer,
       making bounds arithmetic (`len(arr) - 1`) safe even for an empty list.
    2. Integer Overflow:
       In C++, calculating the midpoint as `(left + right) / 2` risks 32-bit integer overflow
       for large indices (often written as `left + (right - left) / 2`). In Python, integers have
       arbitrary precision, so `(left + right) // 2` is inherently safe from integer overflow.
    3. Type Flexibility & Slicing:
       In C++, function templates or type signatures (`template <typename T>`) are required to support
       different numeric types, and passing subvectors incurs memory copying unless using iterators or
       `std::span`. Python's dynamic typing allows duck-typing comparisons effortlessly.
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


if __name__ == "__main__":
    sample_sorted = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("Sorted list:", sample_sorted)
    
    # Test cases
    targets = [23, 2, 91, 50, -1]
    for t in targets:
        idx = binary_search(sample_sorted, t)
        print(f"Search for {t}: index {idx}")
