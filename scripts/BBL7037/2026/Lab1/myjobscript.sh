############# Script for running on HPC using qsub direct submission ############################
### This assume the data has been transfered to HPC using scp command given in doc

#!/bin/bash
#$ -N gnom_stats
#$ -cwd
#$ -j y
#$ -o gnom_stats_$JOB_ID.out

module load compiler/intel/2019u5/intelpython3

echo "Job started on $(date)"
echo "Running on node: $(hostname)"

# Unzip the genome file
gunzip /home/sire/phd/kerberosID/lab1_data/*.gz

# Run the Python script
python3 /home/sire/phd/kerberosID/lab1_data/gnom_stats.py /home/sire/phd/kerberosID/lab1_data/GCF_000005845.2_ASM584v2_genomic.fna

echo "Job finished on $(date)"

