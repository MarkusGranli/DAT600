"""
Compare execution times between Python and Go implementations
DAT600 Assignment 1 - Task 2
"""

import json
import matplotlib.pyplot as plt
import numpy as np

def load_results(filename):
    """Load timing results from JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

def plot_language_comparison(python_results, go_results, save_path='language_comparison.png'):
    """
    Create a comparison plot showing Python vs Go execution times.
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Execution Time Comparison: Python vs Go', fontsize=16, fontweight='bold')
    
    algorithms = ['insertion_sort', 'merge_sort', 'heap_sort', 'quicksort']
    titles = ['Insertion Sort', 'Merge Sort', 'Heap Sort', 'Quicksort']
    
    colors = {
        'Python': '#3776ab',  # Python blue
        'Go': '#00ADD8'       # Go cyan
    }
    
    for idx, (algo, title) in enumerate(zip(algorithms, titles)):
        ax = axes[idx // 2, idx % 2]
        
        # Find data for this algorithm in both languages
        python_data = next((r for r in python_results if r['algorithm'] == algo), None)
        go_data = next((r for r in go_results if r['algorithm'] == algo), None)
        
        if python_data:
            ax.plot(python_data['sizes'], python_data['times'], 
                   marker='o', linewidth=2, markersize=6,
                   label='Python', color=colors['Python'])
        
        if go_data:
            ax.plot(go_data['sizes'], go_data['times'],
                   marker='s', linewidth=2, markersize=6,
                   label='Go', color=colors['Go'])
        
        ax.set_xlabel('Input Size (n)', fontsize=10)
        ax.set_ylabel('Execution Time (seconds)', fontsize=10)
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Comparison plot saved to {save_path}")
    plt.close()

def generate_comparison_table(python_results, go_results):
    """
    Generate a text table comparing execution times.
    """
    print("\n" + "="*80)
    print("EXECUTION TIME COMPARISON TABLE")
    print("="*80)
    
    algorithms = ['insertion_sort', 'merge_sort', 'heap_sort', 'quicksort']
    labels = {
        'insertion_sort': 'Insertion Sort',
        'merge_sort': 'Merge Sort',
        'heap_sort': 'Heap Sort',
        'quicksort': 'Quicksort'
    }
    
    for algo in algorithms:
        python_data = next((r for r in python_results if r['algorithm'] == algo), None)
        go_data = next((r for r in go_results if r['algorithm'] == algo), None)
        
        print(f"\n{labels[algo]}")
        print("-" * 80)
        print(f"{'Size':<10} {'Python (s)':<15} {'Go (s)':<15} {'Speedup':<15}")
        print("-" * 80)
        
        if python_data and go_data:
            for i, size in enumerate(python_data['sizes']):
                if size in go_data['sizes']:
                    go_idx = go_data['sizes'].index(size)
                    py_time = python_data['times'][i]
                    go_time = go_data['times'][go_idx]
                    
                    # Handle cases where Go is too fast to measure
                    if go_time > 0:
                        speedup = py_time / go_time
                        print(f"{size:<10} {py_time:<15.6f} {go_time:<15.6f} {speedup:<15.2f}x")
                    else:
                        print(f"{size:<10} {py_time:<15.6f} {go_time:<15.6f} {'> 1000':<15}x (too fast to measure)")

def main():
    print("Loading experimental results...")
    
    try:
        # Load results from JSON files
        with open('results/timing_results_python.json', 'r') as f:
            python_file = json.load(f)
            # Python file format: {algo_name: {sizes: [], times: []}}
            if isinstance(python_file, dict) and 'insertion_sort' in python_file:
                # Convert to list format
                python_results = []
                for algo_name, data in python_file.items():
                    python_results.append({
                        'algorithm': algo_name,
                        'sizes': data['sizes'],
                        'times': data['times']
                    })
            else:
                python_results = python_file['results'] if 'results' in python_file else python_file
        
        with open('results/timing_results_go.json', 'r') as f:
            go_data = json.load(f)
            go_results = go_data['results'] if isinstance(go_data, dict) and 'results' in go_data else go_data
        
        print("Results loaded successfully!")
        
        # Generate comparison plots
        plot_language_comparison(python_results, go_results, 
                                'results/language_comparison.png')
        
        # Generate comparison table
        generate_comparison_table(python_results, go_results)
        
        print("\n" + "="*80)
        print("TASK 2 ANALYSIS COMPLETE")
        print("="*80)
        print("\nGenerated files:")
        print("  - results/language_comparison.png")
        print("\nThis plot shows the performance differences between Python and Go,")
        print("demonstrating how compiled languages typically outperform interpreted ones.")
        
    except FileNotFoundError as e:
        print(f"Error: Could not find results file: {e}")
        print("Make sure to run both Python and Go experiments first!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
