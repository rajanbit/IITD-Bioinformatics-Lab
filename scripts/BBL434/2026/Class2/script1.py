###### Gemini Code | Vibe Coding Tutorial ######

import sys
import os
from collections import defaultdict
import matplotlib.pyplot as plt

def read_fasta(file_path):
    """Reads a FASTA file and returns the concatenated sequence."""
    sequence = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if not line.startswith('>'):
                    sequence.append(line.strip().upper())
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    return "".join(sequence)

def get_kmer_enrichment(sequence, k, window_size, step):
    """Calculates max k-mer frequency in sliding windows."""
    coordinates = []
    max_counts = []
    window_details = []

    for i in range(0, len(sequence) - window_size + 1, step):
        window = sequence[i : i + window_size]
        counts = defaultdict(int)
        
        # Count all k-mers in the current window
        for j in range(len(window) - k + 1):
            kmer = window[j : j + k]
            counts[kmer] += 1
        
        # Find the most frequent k-mer in this window
        if counts:
            best_kmer = max(counts, key=counts.get)
            max_val = counts[best_kmer]
            
            mid_point = i + (window_size // 2)
            coordinates.append(mid_point)
            max_counts.append(max_val)
            window_details.append((mid_point, best_kmer, max_val))

    return coordinates, max_counts, window_details

def main():
    if len(sys.argv) != 2:
        print("Usage: python script1.py <genomic.fa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    output_plot = "script1_plot1.png"
    
    # Parameters
    K = 8
    WINDOW = 5000
    STEP = 500

    print(f"Reading {fasta_file}...")
    genome = read_fasta(fasta_file)
    
    print(f"Analyzing genome (Length: {len(genome)} bp)...")
    coords, counts, details = get_kmer_enrichment(genome, K, WINDOW, STEP)

    # Identify the overall peak (potential ORI)
    peak_idx = counts.index(max(counts))
    peak_coord, peak_kmer, peak_val = details[peak_idx]

    print("-" * 30)
    print(f"Peak Analysis Results:")
    print(f"Coordinate (mid-window): {peak_coord}")
    print(f"Overrepresented k-mer:  {peak_kmer}")
    print(f"Occurrence Count:       {peak_val}")
    print("-" * 30)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(coords, counts, color='teal', linewidth=1)
    plt.axvline(x=peak_coord, color='red', linestyle='--', alpha=0.5, label=f"Peak at {peak_coord}")
    
    plt.title(f"K-mer Enrichment (k={K}, Window={WINDOW})")
    plt.xlabel("Genomic Position (bp)")
    plt.ylabel(f"Max Frequency of any {K}-mer")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig(output_plot)
    print(f"Plot saved as {output_plot}")

if __name__ == "__main__":
    main()
