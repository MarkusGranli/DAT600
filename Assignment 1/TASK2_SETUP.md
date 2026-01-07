# Task 2 Setup Guide

## Installing Go

Since Go isn't installed yet, follow these steps:

### Windows Installation

1. **Download Go**:
   - Visit: https://go.dev/dl/
   - Download the Windows installer (e.g., `go1.21.x.windows-amd64.msi`)

2. **Install**:
   - Run the MSI installer
   - Follow the installation wizard
   - Go will be installed to `C:\Program Files\Go` by default

3. **Verify Installation**:
   ```powershell
   go version
   ```
   You should see something like: `go version go1.21.x windows/amd64`

4. **Restart PowerShell** after installation to refresh environment variables

## Running the Experiments

### Step 1: Run Python Experiments (Already Done ✓)
```bash
python experiment_runner.py
```

### Step 2: Run Go Experiments
```bash
cd go
go run .
```

This will:
- Compile and run the Go program
- Time all 4 sorting algorithms
- Save results to `../results/timing_results_go.json`

### Step 3: Generate Comparison Plots
```bash
cd ..
python compare_languages.py
```

This creates:
- **language_comparison.png** - Shows Python vs Go side-by-side for each algorithm
- **speedup_analysis.png** - Shows the speedup factor (how many times faster Go is)

## What to Include in Your Report

### For Task 2, discuss:

1. **Performance Differences**:
   - Quantify the speedup (e.g., "Go is 50x faster for insertion sort at n=5000")
   - Note which algorithm benefits most from compilation

2. **Language Characteristics**:
   - **Python**: Interpreted, dynamic typing, easier to write, slower execution
   - **Go**: Compiled, static typing, more verbose, much faster execution

3. **Observations**:
   - Both languages show the same asymptotic complexity (Θ(n²) vs Θ(n lg n))
   - The constant factors differ significantly between languages
   - Go's advantage is more pronounced for simple operations

4. **Plots for LaTeX**:
   ```latex
   \begin{figure}[h]
       \centering
       \includegraphics[width=0.9\textwidth]{language_comparison.png}
       \caption{Execution time comparison between Python and Go implementations}
   \end{figure}
   ```

## Troubleshooting

### If Go installation fails:
- Make sure you have administrator privileges
- Use the official installer from go.dev
- Restart your computer if environment variables don't update

### If go run fails:
- Make sure you're in the `go/` directory
- Check that `go.mod` exists
- Try `go mod tidy` first

### If plots don't generate:
- Make sure both JSON files exist in `results/`
- Check that matplotlib is installed
- Verify the file paths in compare_languages.py
