import time
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Generate a larger array with random numbers
arr = [random.randint(1, 1000) for _ in range(1000)]

# Timing selection sort
start_time = time.time()
sorted_arr = selection_sort(arr.copy())
end_time = time.time()

execution_time = (end_time - start_time) * 1000

print("\nSelection Sort:")
print("Sorted array is:", sorted_arr)
print("Execution time:", execution_time, "seconds")
