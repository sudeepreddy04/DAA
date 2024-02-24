import time
import random

def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return arr, swap_count

# Generate a larger array with random numbers
arr = [random.randint(1, 1000) for _ in range(1000)]

# Timing bubble sort
start_time = time.time()
sorted_arr, swaps = bubble_sort(arr.copy())
end_time = time.time()

execution_time = (end_time - start_time) * 1000

print("\nBubble Sort:")
print("Sorted array is:", sorted_arr)
print("Number of swaps:", swaps)
print("Execution time:", execution_time, "seconds")
