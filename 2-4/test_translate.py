import pytest
from translate import (
    binary_search,
    insertion_sort,
    transpose_matrix,
    sieve_of_eratosthenes,
    get_frequencies,
    merge_sorted_arrays,
    reverse_words
)

# --- Task 1: Binary Search Tests ---
def test_binary_search_middle():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2

def test_binary_search_first_element():
    assert binary_search([10, 20, 30, 40], 10) == 0

def test_binary_search_last_element():
    assert binary_search([10, 20, 30, 40], 40) == 3

def test_binary_search_not_found():
    assert binary_search([1, 2, 4, 5], 3) == -1

def test_binary_search_empty_list():
    assert binary_search([], 5) == -1

# --- Task 2: Insertion Sort Tests ---
def test_insertion_sort_unsorted():
    assert insertion_sort([4, 2, 7, 1, 3]) == [1, 2, 3, 4, 7]

def test_insertion_sort_already_sorted():
    assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_insertion_sort_reverse_sorted():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_insertion_sort_duplicates():
    assert insertion_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

def test_insertion_sort_empty_list():
    assert insertion_sort([]) == []

# --- Task 3: Matrix Transpose Tests ---
def test_transpose_square_matrix():
    assert transpose_matrix([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_transpose_rectangular_wide():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

def test_transpose_rectangular_tall():
    assert transpose_matrix([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]

def test_transpose_single_row():
    assert transpose_matrix([[1, 2, 3, 4]]) == [[1], [2], [3], [4]]

def test_transpose_empty_matrix():
    assert transpose_matrix([]) == []

# --- Task 4: Sieve of Eratosthenes Tests ---
def test_sieve_standard_number():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

def test_sieve_n_is_prime_inclusive():
    assert sieve_of_eratosthenes(11) == [2, 3, 5, 7, 11]

def test_sieve_smallest_prime():
    assert sieve_of_eratosthenes(2) == [2]

def test_sieve_no_primes_one():
    assert sieve_of_eratosthenes(1) == []

def test_sieve_negative_number():
    assert sieve_of_eratosthenes(-5) == []

# --- Task 5: Frequencies Tests ---
def test_frequencies_standard_integers():
    assert get_frequencies([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}

def test_frequencies_strings():
    assert get_frequencies(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}

def test_frequencies_all_unique():
    assert get_frequencies([10, 20, 30]) == {10: 1, 20: 1, 30: 1}

def test_frequencies_all_identical():
    assert get_frequencies([5, 5, 5, 5]) == {5: 4}

def test_frequencies_empty_list():
    assert get_frequencies([]) == {}

# --- Task 6: Merge Sorted Arrays Tests ---
def test_merge_standard_arrays():
    assert merge_sorted_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_different_lengths():
    assert merge_sorted_arrays([1, 2], [3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_with_duplicates():
    assert merge_sorted_arrays([1, 3, 5], [1, 3, 5]) == [1, 1, 3, 3, 5, 5]

def test_merge_one_empty_array():
    assert merge_sorted_arrays([], [1, 2, 3]) == [1, 2, 3]

def test_merge_both_empty():
    assert merge_sorted_arrays([], []) == []

# --- Task 7: Reverse Words Tests ---
def test_reverse_words_standard_sentence():
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_multiple_words():
    assert reverse_words("the quick brown fox") == "fox brown quick the"

def test_reverse_words_single_word():
    assert reverse_words("python") == "python"

def test_reverse_words_extra_whitespace():
    assert reverse_words("  hello   world  ") == "world hello"

def test_reverse_words_empty_string():
    assert reverse_words("") == ""