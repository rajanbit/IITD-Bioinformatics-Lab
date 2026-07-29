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

def get_all_clump_kmers(sequence, k, L, t):
    """
    Identifies every unique k-mer that forms a clump within 
    at least one window of length L.
    """
    n = len(sequence)
    all_clump_kmers = set()
    
    # 1. Initialize the first window [0 : L]
    counts = defaultdict(int)
    for j in range(L - k + 1):
        kmer = sequence[j : j + k]
        counts[kmer] += 1
    
    # Check for clumps in the first window
    for kmer, count in counts.items():
        if count >= t:
            all_clump_kmers.add(kmer)

    # 2. Slide the window across the genome
    for i in range(1, n - L + 1):
        # Remove the k-mer sliding out
        out_kmer = sequence[i - 1 : i - 1 + k]
        counts[out_kmer] -= 1
        
        # Add the k-mer sliding in
        in_kmer = sequence[i + L - k : i + L]
        counts[in_kmer] += 1
        
        # If the incoming k-mer hits the threshold in the current window
        if counts[in_kmer] >= t:
            all_clump_kmers.add(in_kmer)

    return sorted(list(all_clump_kmers))

def main():
    if len(sys.argv) != 2:
        print("Usage: python clump_list.py <genomic.fa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    
    # Parameters
    K, L, T = 8, 1000, 3

    print(f"# Processing: {fasta_file}")
    print(f"# Parameters: k={K}, L={L}, t={T}")
    
    genome = read_fasta(fasta_file)
    clump_kmers = get_all_clump_kmers(genome, K, L, T)

    if clump_kmers:
        print(f"# Found {len(clump_kmers)} unique clump-forming k-mers:")
        for kmer in clump_kmers[:3]: # Print first 3 kmers
            print(kmer)
    else:
        print("# No clumps found with the current parameters.")

if __name__ == "__main__":
    main()
