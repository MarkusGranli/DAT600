# DAT600 Assignment 1: Sorting Algorithms and Running Time Analysis

This repository contains implementations and experiments for Assignment 1 in DAT600 Algorithm Theory.

## Assignment Overview

The assignment covers:
1. **Task 1**: Implementation of four sorting algorithms with step counting
2. **Task 2**: Comparative execution time analysis across programming languages
3. **Task 3**: Mathematical proofs using Big-O notation
4. **Task 4**: Master Theorem and recurrence relation analysis

## Repository Structure

```
DAT600/
├── sorting_algorithms.py      # Core sorting algorithm implementations
├── experiment_runner.py        # Experiment runner and plotting
├── requirements.txt            # Python dependencies
├── results/                    # Generated plots and data
│   ├── step_counts_random.png
│   ├── execution_times_python.png
│   └── *.json                  # Raw experimental data
└── README.md
```

## Implemented Algorithms

All algorithms include step counting to verify theoretical complexity:

| Algorithm | Worst-case Complexity | Implementation Status |
|-----------|----------------------|----------------------|
| Insertion Sort | Θ(n²) | ✓ Complete |
| Merge Sort | Θ(n lg n) | ✓ Complete |
| Heap Sort | O(n lg n) | ✓ Complete |
| Quicksort | Θ(n²) | ✓ Complete |

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd DAT600
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Experiments

### Task 1: Step Counting and Plotting

Run all experiments and generate plots:
```bash
python experiment_runner.py
```

This will:
- Test all four sorting algorithms with varying input sizes
- Count the number of operations for each
- Generate plots showing step counts vs. input size
- Save results as high-resolution images for LaTeX reports
- Export raw data as JSON files

### Testing Individual Algorithms

```bash
python sorting_algorithms.py
```

## Results

### Step Counting (Task 1)

The experiments verify the theoretical time complexities:

- **Insertion Sort**: Shows quadratic growth (n²) in step count
- **Merge Sort**: Shows linearithmic growth (n lg n)
- **Heap Sort**: Shows linearithmic growth (n lg n)
- **Quicksort**: Depends on input; worst case shows quadratic growth

All generated plots are saved with 300 DPI resolution, suitable for inclusion in LaTeX documents.

### Performance Observations

Key findings from the experiments:
1. Merge Sort and Heap Sort consistently outperform Insertion Sort for larger inputs
2. Quicksort performs well on random data but degrades on sorted/reverse-sorted data
3. Step counts closely match theoretical predictions

## Task 2: Multi-Language Comparison

### Go Implementation

The Go implementation provides the same sorting algorithms for performance comparison:

**Location**: `go/` directory
- `sorting_algorithms.go` - All 4 sorting algorithms
- `main.go` - Timing experiments and JSON export
- `go.mod` - Go module file

### Running Go Experiments

```bash
cd go
go run .
```

This will:
- Run timing experiments with the same input sizes as Python
- Export results to `results/timing_results_go.json`
- Test both random and sorted arrays

### Comparing Python vs Go

After running both Python and Go experiments:

```bash
python compare_languages.py
```

This generates:
- `language_comparison.png` - Side-by-side comparison of all algorithms
- `speedup_analysis.png` - Shows how much faster Go is than Python
- Console table with detailed timing comparisons

### Expected Observations

- **Go is typically 10-100x faster** than Python for these algorithms
- Compiled languages (Go) have less overhead than interpreted languages (Python)
- The performance gap is larger for simple operations (like insertion sort)
- Both languages show the same asymptotic complexity patterns
