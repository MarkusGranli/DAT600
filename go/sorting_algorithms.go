package main

import (
	"math/rand"
)

// InsertionSort sorts an array using insertion sort
// Returns the sorted array and the number of operations
func InsertionSort(arr []int) ([]int, int) {
	result := make([]int, len(arr))
	copy(result, arr)
	n := len(result)
	steps := 0

	for i := 1; i < n; i++ {
		key := result[i]
		j := i - 1
		steps++ // Outer loop iteration

		for j >= 0 && result[j] > key {
			steps++ // Comparison
			result[j+1] = result[j]
			j--
		}

		if j >= 0 {
			steps++ // Final comparison that failed
		}

		result[j+1] = key
	}

	return result, steps
}

// MergeSort sorts an array using merge sort
// Returns the sorted array and the number of operations
func MergeSort(arr []int) ([]int, int) {
	result := make([]int, len(arr))
	copy(result, arr)
	steps := 0

	var merge func([]int, int, int, int)
	merge = func(arr []int, left, mid, right int) {
		// Create temp arrays
		leftSize := mid - left + 1
		rightSize := right - mid

		L := make([]int, leftSize)
		R := make([]int, rightSize)

		copy(L, arr[left:mid+1])
		copy(R, arr[mid+1:right+1])

		i, j, k := 0, 0, left

		// Merge the temp arrays back
		for i < leftSize && j < rightSize {
			steps++ // Comparison
			if L[i] <= R[j] {
				arr[k] = L[i]
				i++
			} else {
				arr[k] = R[j]
				j++
			}
			k++
		}

		// Copy remaining elements
		for i < leftSize {
			steps++
			arr[k] = L[i]
			i++
			k++
		}

		for j < rightSize {
			steps++
			arr[k] = R[j]
			j++
			k++
		}
	}

	var mergeSortHelper func([]int, int, int)
	mergeSortHelper = func(arr []int, left, right int) {
		if left < right {
			steps++ // Split operation
			mid := left + (right-left)/2
			mergeSortHelper(arr, left, mid)
			mergeSortHelper(arr, mid+1, right)
			merge(arr, left, mid, right)
		}
	}

	mergeSortHelper(result, 0, len(result)-1)
	return result, steps
}

// HeapSort sorts an array using heap sort
// Returns the sorted array and the number of operations
func HeapSort(arr []int) ([]int, int) {
	result := make([]int, len(arr))
	copy(result, arr)
	n := len(result)
	steps := 0

	var heapify func([]int, int, int)
	heapify = func(arr []int, n, i int) {
		largest := i
		left := 2*i + 1
		right := 2*i + 2

		if left < n {
			steps++ // Comparison
			if arr[left] > arr[largest] {
				largest = left
			}
		}

		if right < n {
			steps++ // Comparison
			if arr[right] > arr[largest] {
				largest = right
			}
		}

		if largest != i {
			steps++ // Swap operation
			arr[i], arr[largest] = arr[largest], arr[i]
			heapify(arr, n, largest)
		}
	}

	// Build max heap
	for i := n/2 - 1; i >= 0; i-- {
		steps++
		heapify(result, n, i)
	}

	// Extract elements from heap one by one
	for i := n - 1; i > 0; i-- {
		steps++ // Swap
		result[0], result[i] = result[i], result[0]
		heapify(result, i, 0)
	}

	return result, steps
}

// QuickSort sorts an array using quicksort
// Returns the sorted array and the number of operations
func QuickSort(arr []int) ([]int, int) {
	result := make([]int, len(arr))
	copy(result, arr)
	steps := 0

	var partition func([]int, int, int) int
	partition = func(arr []int, low, high int) int {
		pivot := arr[high]
		i := low - 1

		for j := low; j < high; j++ {
			steps++ // Comparison
			if arr[j] <= pivot {
				i++
				arr[i], arr[j] = arr[j], arr[i]
			}
		}

		arr[i+1], arr[high] = arr[high], arr[i+1]
		return i + 1
	}

	var quickSortHelper func([]int, int, int)
	quickSortHelper = func(arr []int, low, high int) {
		if low < high {
			steps++ // Partition operation
			pi := partition(arr, low, high)
			quickSortHelper(arr, low, pi-1)
			quickSortHelper(arr, pi+1, high)
		}
	}

	quickSortHelper(result, 0, len(result)-1)
	return result, steps
}

// GenerateRandomArray creates a random array of given size
func GenerateRandomArray(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = rand.Intn(10000)
	}
	return arr
}

// GenerateSortedArray creates a sorted array
func GenerateSortedArray(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = i
	}
	return arr
}

// GenerateReverseSortedArray creates a reverse sorted array
func GenerateReverseSortedArray(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = size - i
	}
	return arr
}
