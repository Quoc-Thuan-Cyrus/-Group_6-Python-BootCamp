#task 6

def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    return sorted([*arr1, *arr2])


# Kiểm thử
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

print(merge_sorted_arrays(arr1, arr2))
# Output: [1, 2, 3, 4, 5, 6, 7, 8]