import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Generate a larger array with random numbers
arr = [random.randint(1, 1000) for _ in range(1000)]

# Timing insertion sort
start_time = time.time()
sorted_arr = insertion_sort(arr.copy())
end_time = time.time()

execution_time = (end_time - start_time) * 1000

print("\nInsertion Sort:")
print("Sorted array is:", sorted_arr)
print("Execution time:", execution_time, "seconds")
