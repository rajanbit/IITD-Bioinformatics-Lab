# Importing module
from Bio.Seq import Seq

# Creating Seq object
dna = Seq("ATGAAATTT")
print(f"DNA: {dna}")

# Transcription
rna = dna.transcribe()
print(f"RNA: {rna}")

# Translation
prot = rna.translate()
print(f"Protein: {prot}")
