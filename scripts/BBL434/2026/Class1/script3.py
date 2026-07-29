#!/usr/bin/env python3

###### ChatGPT Code | Vibe Coding Tutorial ######

import sys

if len(sys.argv) != 2:
    print("Usage: python count_fasta_records.py <fasta_file>")
    sys.exit(1)

fasta_file = sys.argv[1]
count = 0

try:
    with open(fasta_file, "r") as f:
        for line in f:
            if line.startswith(">"):
                count += 1

    print(count)

except FileNotFoundError:
    print(f"Error: File '{fasta_file}' not found.")

