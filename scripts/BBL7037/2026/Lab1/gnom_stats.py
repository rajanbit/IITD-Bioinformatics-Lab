# Importing modules
import sys
from collections import Counter

# Function to generate genome stats
# ChatGPT generated code
def genome_statistics(fasta_file):

    sequence = ""

    with open(fasta_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            sequence += line.upper()

    genome_length = len(sequence)

    counts = Counter(sequence)

    A = counts.get("A", 0)
    T = counts.get("T", 0)
    G = counts.get("G", 0)
    C = counts.get("C", 0)

    canonical = A + T + G + C
    others = genome_length - canonical

    gc_content = ((G + C) / canonical * 100) if canonical else 0
    at_content = ((A + T) / canonical * 100) if canonical else 0

    with open("output.txt", "w") as out:
        out.write("=" * 50 + "\n")
        out.write("Genome Statistics\n")
        out.write("=" * 50 + "\n")
        out.write(f"Genome Length : {genome_length:,} bp\n")
        out.write(f"A             : {A:,}\n")
        out.write(f"T             : {T:,}\n")
        out.write(f"G             : {G:,}\n")
        out.write(f"C             : {C:,}\n")
        out.write(f"Other Bases   : {others:,}\n")
        out.write("-" * 50 + "\n")
        out.write(f"GC Content    : {gc_content:.2f}%\n")
        out.write(f"AT Content    : {at_content:.2f}%\n")
        out.write("=" * 50 + "\n")

# Run
genome_statistics(sys.argv[1])

