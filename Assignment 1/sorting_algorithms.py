"""
Sorting Algorithms with Step Counting
DAT600 Assignment 1 - Task 1

Implements four sorting algorithms with step counting:
- Insertion Sort: Θ(n²)
- Merge Sort: Θ(n lg n)
- Heap Sort: O(n lg n)
- Quicksort: Θ(n²) worst-case
"""

def insertion_sort(arr):
    """
    Insertion Sort with step counting.
    Returns: (sorted_array, step_count)
    """
    arr = arr.copy()
    n = len(arr)
    steps = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        steps += 1  # Outer loop iteration
        
        while j >= 0 and arr[j] > key:
            steps += 1  # Comparison
            arr[j + 1] = arr[j]
            j -= 1
        
        if j >= 0:
            steps += 1  # Final comparison that failed
        
        arr[j + 1] = key
    
    return arr, steps


def merge_sort(arr):
    """
    Merge Sort with step counting.
    Returns: (sorted_array, step_count)
    """
    arr = arr.copy()
    steps = [0]
    
    def merge(arr, left, mid, right):
        # Create temp arrays
        L = arr[left:mid+1]
        R = arr[mid+1:right+1]
        
        i = j = 0
        k = left
        
        # Merge the temp arrays back
        while i < len(L) and j < len(R):
            steps[0] += 1  # Comparison
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Copy remaining elements
        while i < len(L):
            steps[0] += 1
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            steps[0] += 1
            arr[k] = R[j]
            j += 1
            k += 1
    
    def merge_sort_helper(arr, left, right):
        if left < right:
            steps[0] += 1  # Split operation
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)
    
    merge_sort_helper(arr, 0, len(arr) - 1)
    return arr, steps[0]


def heap_sort(arr):
    """
    Heap Sort with step counting.
    Returns: (sorted_array, step_count)
    """
    arr = arr.copy()
    n = len(arr)
    steps = [0]
    
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n:
            steps[0] += 1  # Comparison
            if arr[left] > arr[largest]:
                largest = left
        
        if right < n:
            steps[0] += 1  # Comparison
            if arr[right] > arr[largest]:
                largest = right
        
        if largest != i:
            steps[0] += 1  # Swap operation
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        steps[0] += 1
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        steps[0] += 1  # Swap
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr, steps[0]


def quicksort(arr):
    """
    Quicksort with step counting.
    Uses last element as pivot (worst case on sorted arrays).
    Returns: (sorted_array, step_count)
    """
    arr = arr.copy()
    steps = [0]
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            steps[0] += 1  # Comparison
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quicksort_helper(arr, low, high):
        if low < high:
            steps[0] += 1  # Partition operation
            pi = partition(arr, low, high)
            quicksort_helper(arr, low, pi - 1)
            quicksort_helper(arr, pi + 1, high)
    
    quicksort_helper(arr, 0, len(arr) - 1)
    return arr, steps[0]


if __name__ == "__main__":
    # Simple test
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_arr)
    
    sorted_arr, steps = insertion_sort(test_arr)
    print(f"Insertion Sort: {sorted_arr}, Steps: {steps}")
    
    sorted_arr, steps = merge_sort(test_arr)
    print(f"Merge Sort: {sorted_arr}, Steps: {steps}")
    
    sorted_arr, steps = heap_sort(test_arr)
    print(f"Heap Sort: {sorted_arr}, Steps: {steps}")
    
    sorted_arr, steps = quicksort(test_arr)
    print(f"Quicksort: {sorted_arr}, Steps: {steps}")
