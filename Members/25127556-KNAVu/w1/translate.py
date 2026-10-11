def binary_search(a: list[int], key: int) -> int:
    """Binary search implementation in Python.
    
    Difference from C++: Python lists dynamic sizing and explicit bounds check
    handling without pointers or iterator types.
    """
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == key:
            return mid
        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1