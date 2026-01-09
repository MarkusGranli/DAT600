"""
Experiment Runner for Sorting Algorithms
DAT600 Assignment 1 - Task 1

Runs experiments with varying input sizes and generates plots
for LaTeX report.
"""

import numpy as np
import matplotlib.pyplot as plt
from sorting_algorithms import insertion_sort, merge_sort, heap_sort, quicksort
import time
import json

def generate_random_array(size):
    """Generate a random array of given size."""
    return np.random.randint(0, 10000, size).tolist()

def generate_sorted_array(size):
    """Generate a sorted array (worst case for quicksort)."""
    return list(range(size))

def generate_reverse_sorted_array(size):
    """Generate a reverse sorted array (worst case for insertion sort)."""
    return list(range(size, 0, -1))

def run_step_counting_experiments(sizes, array_type='random'):
    """
    Run experiments to count steps for all sorting algorithms.
    
    Args:
        sizes: List of input sizes to test
        array_type: 'random', 'sorted', or 'reverse'
    
    Returns:
        Dictionary with results for each algorithm
    """
    results = {
        'insertion_sort': {'sizes': [], 'steps': []},
        'merge_sort': {'sizes': [], 'steps': []},
        'heap_sort': {'sizes': [], 'steps': []},
        'quicksort': {'sizes': [], 'steps': []}
    }
    
    algorithms = {
        'insertion_sort': insertion_sort,
        'merge_sort': merge_sort,
        'heap_sort': heap_sort,
        'quicksort': quicksort
    }
    
    print(f"\nRunning step counting experiments with {array_type} arrays...")
    
    for size in sizes:
        print(f"Testing size n={size}...")
        
        # Generate test array
        if array_type == 'random':
            test_arr = generate_random_array(size)
        elif array_type == 'sorted':
            test_arr = generate_sorted_array(size)
        else:  # reverse
            test_arr = generate_reverse_sorted_array(size)
        
        for algo_name, algo_func in algorithms.items():
            try:
                _, steps = algo_func(test_arr)
                results[algo_name]['sizes'].append(size)
                results[algo_name]['steps'].append(steps)
            except Exception as e:
                print(f"Error with {algo_name} at size {size}: {e}")
    
    return results

def run_timing_experiments(sizes, array_type='random', runs=3):
    """
    Run experiments to measure actual execution time.
    
    Args:
        sizes: List of input sizes to test
        array_type: 'random', 'sorted', or 'reverse'
        runs: Number of runs to average
    
    Returns:
        Dictionary with timing results for each algorithm
    """
    results = {
        'insertion_sort': {'sizes': [], 'times': []},
        'merge_sort': {'sizes': [], 'times': []},
        'heap_sort': {'sizes': [], 'times': []},
        'quicksort': {'sizes': [], 'times': []}
    }
    
    algorithms = {
        'insertion_sort': insertion_sort,
        'merge_sort': merge_sort,
        'heap_sort': heap_sort,
        'quicksort': quicksort
    }
    
    print(f"\nRunning timing experiments with {array_type} arrays...")
    
    for size in sizes:
        print(f"Testing size n={size}...")
        
        for algo_name, algo_func in algorithms.items():
            times = []
            for _ in range(runs):
                # Generate fresh array for each run
                if array_type == 'random':
                    test_arr = generate_random_array(size)
                elif array_type == 'sorted':
                    test_arr = generate_sorted_array(size)
                else:  # reverse
                    test_arr = generate_reverse_sorted_array(size)
                
                start_time = time.perf_counter()
                algo_func(test_arr)
                end_time = time.perf_counter()
                times.append(end_time - start_time)
            
            avg_time = np.mean(times)
            results[algo_name]['sizes'].append(size)
            results[algo_name]['times'].append(avg_time)
    
    return results

def plot_step_counts(results, array_type='random', save_path='step_counts.png'):
    """
    Plot step counts for all algorithms.
    Creates publication-quality plot for LaTeX.
    """
    plt.figure(figsize=(10, 6))
    
    colors = {
        'insertion_sort': '#e74c3c',
        'merge_sort': '#3498db',
        'heap_sort': '#2ecc71',
        'quicksort': '#f39c12'
    }
    
    labels = {
        'insertion_sort': 'Insertion Sort (Θ(n²))',
        'merge_sort': 'Merge Sort (Θ(n lg n))',
        'heap_sort': 'Heap Sort (O(n lg n))',
        'quicksort': 'Quicksort (Θ(n²) worst)'
    }
    
    for algo_name, data in results.items():
        if data['sizes']:
            plt.plot(data['sizes'], data['steps'], 
                    marker='o', linewidth=2, markersize=6,
                    label=labels[algo_name], color=colors[algo_name])
    
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Number of Steps', fontsize=12)
    plt.title(f'Step Count Comparison - {array_type.capitalize()} Arrays', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to {save_path}")
    plt.close()

def plot_timing_results(results, array_type='random', save_path='execution_times.png'):
    """
    Plot execution times for all algorithms.
    """
    plt.figure(figsize=(10, 6))
    
    colors = {
        'insertion_sort': '#e74c3c',
        'merge_sort': '#3498db',
        'heap_sort': '#2ecc71',
        'quicksort': '#f39c12'
    }
    
    labels = {
        'insertion_sort': 'Insertion Sort',
        'merge_sort': 'Merge Sort',
        'heap_sort': 'Heap Sort',
        'quicksort': 'Quicksort'
    }
    
    for algo_name, data in results.items():
        if data['sizes']:
            plt.plot(data['sizes'], data['times'], 
                    marker='o', linewidth=2, markersize=6,
                    label=labels[algo_name], color=colors[algo_name])
    
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title(f'Execution Time Comparison - {array_type.capitalize()} Arrays', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to {save_path}")
    plt.close()

def save_results_json(results, filename='results.json'):
    """Save results to JSON file for later analysis."""
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {filename}")

if __name__ == "__main__":
    # Define test sizes
    small_sizes = [10, 20, 50, 100, 200, 500, 1000]
    medium_sizes = [10, 50, 100, 500, 1000, 2000, 5000]
    
    # Task 1: Step counting with random arrays
    print("=" * 60)
    print("TASK 1: Step Counting Experiments")
    print("=" * 60)
    
    step_results = run_step_counting_experiments(medium_sizes, array_type='random')
    plot_step_counts(step_results, array_type='random', save_path='step_counts_random.png')
    save_results_json(step_results, 'step_counts_random.json')
    
    # Additional: worst-case scenarios
    print("\n" + "=" * 60)
    print("Worst Case Scenarios")
    print("=" * 60)
    
    # Reverse sorted (worst for insertion sort)
    step_results_worst = run_step_counting_experiments(small_sizes, array_type='reverse')
    plot_step_counts(step_results_worst, array_type='reverse', save_path='step_counts_worst.png')
    
    # Sorted (worst for quicksort with last element pivot)
    step_results_sorted = run_step_counting_experiments(small_sizes, array_type='sorted')
    plot_step_counts(step_results_sorted, array_type='sorted', save_path='step_counts_sorted.png')
    
    # Task 2 prep: Timing experiments
    print("\n" + "=" * 60)
    print("TASK 2: Timing Experiments (Python)")
    print("=" * 60)
    
    timing_results = run_timing_experiments(medium_sizes, array_type='random', runs=5)
    plot_timing_results(timing_results, array_type='random', save_path='execution_times_python.png')
    save_results_json(timing_results, 'timing_results_python.json')
    
    print("\n" + "=" * 60)
    print("All experiments completed!")
    print("=" * 60)
