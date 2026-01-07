package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"os"
	"time"
)

// TimingResult stores timing information for an algorithm
type TimingResult struct {
	Algorithm string    `json:"algorithm"`
	Sizes     []int     `json:"sizes"`
	Times     []float64 `json:"times"`
}

// ExperimentResults stores all timing results
type ExperimentResults struct {
	Language  string         `json:"language"`
	ArrayType string         `json:"array_type"`
	Timestamp string         `json:"timestamp"`
	Results   []TimingResult `json:"results"`
}

func timeAlgorithm(sortFunc func([]int) ([]int, int), arr []int, runs int) float64 {
	var totalDuration time.Duration

	for i := 0; i < runs; i++ {
		// Create a fresh copy for each run
		testArr := make([]int, len(arr))
		copy(testArr, arr)

		start := time.Now()
		sortFunc(testArr)
		duration := time.Since(start)
		totalDuration += duration
	}

	return totalDuration.Seconds() / float64(runs)
}

func runTimingExperiments(sizes []int, arrayType string, runs int) ExperimentResults {
	fmt.Printf("\nRunning timing experiments with %s arrays...\n", arrayType)

	algorithms := map[string]func([]int) ([]int, int){
		"insertion_sort": InsertionSort,
		"merge_sort":     MergeSort,
		"heap_sort":      HeapSort,
		"quicksort":      QuickSort,
	}

	results := ExperimentResults{
		Language:  "Go",
		ArrayType: arrayType,
		Timestamp: time.Now().Format(time.RFC3339),
		Results:   make([]TimingResult, 0),
	}

	for algoName, algoFunc := range algorithms {
		fmt.Printf("Testing %s...\n", algoName)

		timingResult := TimingResult{
			Algorithm: algoName,
			Sizes:     make([]int, 0),
			Times:     make([]float64, 0),
		}

		for _, size := range sizes {
			fmt.Printf("  Size n=%d...\n", size)

			var arr []int
			switch arrayType {
			case "random":
				arr = GenerateRandomArray(size)
			case "sorted":
				arr = GenerateSortedArray(size)
			case "reverse":
				arr = GenerateReverseSortedArray(size)
			}

			avgTime := timeAlgorithm(algoFunc, arr, runs)

			timingResult.Sizes = append(timingResult.Sizes, size)
			timingResult.Times = append(timingResult.Times, avgTime)
		}

		results.Results = append(results.Results, timingResult)
	}

	return results
}

func saveResultsJSON(results ExperimentResults, filename string) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	encoder.SetIndent("", "  ")
	err = encoder.Encode(results)
	if err != nil {
		return err
	}

	fmt.Printf("Results saved to %s\n", filename)
	return nil
}

func main() {
	// Seed random number generator
	rand.Seed(time.Now().UnixNano())

	fmt.Println("============================================================")
	fmt.Println("DAT600 Assignment 1 - Task 2: Go Implementation")
	fmt.Println("============================================================")

	// Define test sizes - matching Python experiments
	sizes := []int{10, 50, 100, 500, 1000, 2000, 5000}
	runs := 5

	// Run timing experiments with random arrays
	results := runTimingExperiments(sizes, "random", runs)
	err := saveResultsJSON(results, "../results/timing_results_go.json")
	if err != nil {
		fmt.Printf("Error saving results: %v\n", err)
	}

	// Optional: Run with sorted arrays (worst case for quicksort)
	fmt.Println("\n============================================================")
	fmt.Println("Sorted Array Experiments (Worst Case)")
	fmt.Println("============================================================")

	smallSizes := []int{10, 50, 100, 500, 1000}
	sortedResults := runTimingExperiments(smallSizes, "sorted", runs)
	err = saveResultsJSON(sortedResults, "../results/timing_results_go_sorted.json")
	if err != nil {
		fmt.Printf("Error saving results: %v\n", err)
	}

	fmt.Println("\n============================================================")
	fmt.Println("All experiments completed!")
	fmt.Println("============================================================")
}
