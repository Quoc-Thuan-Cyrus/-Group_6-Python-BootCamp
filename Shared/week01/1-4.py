

#task 2
def insertion_sort(arr):
    """
    Sorts a list in-place using the insertion sort algorithm and returns it.
    
    Difference from C++:
    In Python, we do not need to pass the size of the array as a separate 
    parameter (like `int n` in C++) because Python lists inherently know 
    their own length, which can be accessed using `len(arr)`. Additionally, 
    due to Python's dynamic typing, this single function can sort lists of 
    integers, floats, or strings without needing templates or function overloading.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key, 
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr

# Example usage:
# my_list = [12, 11, 13, 5, 6]
# sorted_list = insertion_sort(my_list)
# print(sorted_list)  # Output: [5, 6, 11, 12, 13]