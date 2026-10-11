def transpose(matrix: list[list[any]]) -> list[list[any]]:
    """Transpose a 2D matrix (vector of vectors).

    Example:
        transpose([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]

    Difference from C++ version:
    1. Memory & Types: In C++, transposing a `std::vector<std::vector<T>>`
       requires explicit nested loops, pre-allocating rows and columns
       with fixed data types `T`, and handling indices `[i][j]`.
    2. Pythonic Idiom: In Python, using `zip(*matrix)` combined with list
       comprehension unpacks all rows into column-wise tuples in a single,
       concise, and highly optimized expression, naturally supporting any element types.
    """
    if not matrix or not matrix[0]:
        return []

    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    sample_matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print("Original matrix:")
    for row in sample_matrix:
        print(row)

    transposed = transpose(sample_matrix)
    print("\nTransposed matrix:")
    for row in transposed:
        print(row)
