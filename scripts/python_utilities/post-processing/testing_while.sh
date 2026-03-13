#PBS -A P48503002                                                                                                                                   
#PBS -N FastEddy
#PBS -l select=1:ncpus=4:mpiprocs=4:ngpus=4:mem=100GB
#PBS -l walltime=12:00:00
#PBS -q casper
#PBS -j oe
#PBS -l job_priority=economy#!/bin/bash



condition=True
while [ $condition = True ]; do
   echo "condition = $condition"
   for (( i=0; i<10; i++)); do
      sum=$(($sum+i))
      echo "sum = $sum"
      if [ $sum -gt 5 ]; then
         echo "condition gt 5: $condition"
         condition='False'
         break
         
      fi
   done
