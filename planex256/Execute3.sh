#!/bin/bash

# Copy/paste this job script into a text file and submit with the command:
#    sbatch thefilename
# job standard output will go to the file slurm-%j.out (where %j is the job ID)

#SBATCH --time=20:00:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=1   # 16 processor core(s) per node
#SBATCH --job-name="Exp_256_exe_3"
#SBATCH --output="s%j.out" # job standard output file (%j replaced by job id)

. ../../cnn/bin/activate
cd /home/aapowadi/anirudha/train/planex256/
python Exp_Execute3.py
