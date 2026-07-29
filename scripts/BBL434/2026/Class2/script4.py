###### Gemini Code | Vibe Coding Tutorial ######

import sys
from collections import defaultdict

def read_fasta(file_path):
    """Reads a FASTA file and returns the concatenated sequence."""
    sequence = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('>'):
                    continue
                sequence.append(line.upper())
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    return "".join(sequence)

def find_ori_and_enrichment(sequence, k, window_size, step):
    """
    Calculates Cumulative GC Skew and K-mer Enrichment.
    Returns:
    - ori_coord: Coordinate of the global minimum of cumulative skew.
    - enriched_coord: Center of the window with the highest k-mer frequency.
    - enriched_seq: The specific k-mer sequence found in that window.
    """
    n = len(sequence)
    
    # Skew variables
    cumulative_skew = 0
    min_skew = float('inf')
    ori_coord = 0
    
    # Enrichment variables
    max_count = 0
    enriched_coord = 0
    enriched_seq = ""

    # Sliding Window
    for i in range(0, n - window_size + 1, step):
        window = sequence[i : i + window_size]
        mid_point = i + (window_size // 2)

        # 1. Cumulative GC Skew Calculation
        g = window.count('G')
        c = window.count('C')
        if (g + c) > 0:
            skew = (g - c) / (g + c)
        else:
            skew = 0
        
        cumulative_skew += skew
        if cumulative_skew < min_skew:
            min_skew = cumulative_skew
            ori_coord = mid_point

        # 2. K-mer Enrichment Calculation
        counts = defaultdict(int)
        for j in range(len(window) - k + 1):
            kmer = window[j : j + k]
            counts[kmer] += 1
        
        if counts:
            local_best_kmer = max(counts, key=counts.get)
            local_max_count = counts[local_best_kmer]
            
            if local_max_count > max_count:
                max_count = local_max_count
                enriched_coord = mid_point
                enriched_seq = local_best_kmer

    return ori_coord, enriched_coord, enriched_seq, max_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python script1.py <genomic.fa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    
    # Parameters
    K = 8
    WINDOW = 5000
    STEP = 500

    print(f"# Analyzing: {fasta_file}")
    genome = read_fasta(fasta_file)
    
    ori_loc, enriched_loc, kmer_seq, count = find_ori_and_enrichment(genome, K, WINDOW, STEP)

    print("-" * 50)
    print(f"ORI LOCATION (via Cumulative GC Skew Min):")
    print(f"  Coordinate: {ori_loc} bp")
    print("-" * 50)
    print(f"MOST ENRICHED REGION (via {K}-mer Frequency):")
    print(f"  Center Coordinate: {enriched_loc} bp")
    print(f"  Overrepresented Sequence: {kmer_seq}")
    print(f"  Occurrence Count: {count}")
    print("-" * 50)

if __name__ == "__main__":
    main()
