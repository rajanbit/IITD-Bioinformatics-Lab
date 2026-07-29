###### Gemini Code | Vibe Coding Tutorial ######

import sys
import matplotlib.pyplot as plt

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

def calculate_cumulative_skew(sequence, window_size, step):
    """
    Calculates the cumulative GC skew.
    Returns window center coordinates and cumulative skew values.
    """
    coords = []
    cumulative_values = []
    current_cumulative = 0
    
    # Sliding window logic
    for i in range(0, len(sequence) - window_size + 1, step):
        window = sequence[i : i + window_size]
        g = window.count('G')
        c = window.count('C')
        
        # Calculate local window skew
        if (g + c) > 0:
            skew = (g - c) / (g + c)
        else:
            skew = 0
            
        current_cumulative += skew
        cumulative_values.append(current_cumulative)
        coords.append(i + (window_size // 2))
        
    return coords, cumulative_values

def main():
    if len(sys.argv) != 2:
        print("Usage: python script1.py <genomic.fa>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    output_plot = "script3_plot1.png"
    
    # Parameters
    WINDOW = 5000
    STEP = 500

    print(f"Loading {fasta_file}...")
    genome = read_fasta(fasta_file)
    
    print(f"Calculating Cumulative GC Skew (W={WINDOW}, S={STEP})...")
    coords, skew_data = calculate_cumulative_skew(genome, WINDOW, STEP)

    # Find the global minimum (Potential ORI)
    min_val = min(skew_data)
    min_idx = skew_data.index(min_val)
    ori_coord = coords[min_idx]

    print("-" * 35)
    print(f"Minimum Cumulative Skew: {min_val:.4f}")
    print(f"Potential ORI Coordinate: {ori_coord} bp")
    print("-" * 35)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(coords, skew_data, color='blue', linewidth=1.5, label='Cumulative GC Skew')
    
    # Mark the ORI
    plt.scatter(ori_coord, min_val, color='red', s=50, zorder=5, label=f'Potential ORI ({ori_coord} bp)')
    
    plt.title(f"Cumulative GC Skew Plot (Window={WINDOW}, Step={STEP})")
    plt.xlabel("Genomic Position (bp)")
    plt.ylabel("Cumulative Skew")
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.savefig(output_plot)
    print(f"Plot saved as {output_plot}")

if __name__ == "__main__":
    main()
