###### Script run on lab server ####################

# Download data
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz

# Unzip file
gunzip *.gz

# Run script
python3 gnom_stats.py GCF_000005845.2_ASM584v2_genomic.fna
