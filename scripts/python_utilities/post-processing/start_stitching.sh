#!/bin/bash

# PBS directives go here


# echo $PBS_JOBID
# end PBS directives

echo "Inside testing script"

#module load conda
#conda activate /Volumes/d1/minnawin/miniforge3/envs/fasteddy_env

#export BASEDIR=/glade/u/home/minnawin/FE_Dev/FastEddy-model/
export BASEDIR=/Users/minnawin/FastEddy-model/
export SRCDIR=${BASEDIR}/SRC/FEMAIN/
export CONVERTSRCDIR=${BASEDIR}/scripts/python_utilities/post-processing/

# Provide binary file filename prefix
export BINARYFILEPREFIX=FE_NBL

# Provide sleep time in seconds
export SLEEPSECS=5

# Provide the location to copy files for staging
export STAGINGDIR=/Users/minnawin/FastEddy-model/scripts/python_utilities/post-processing/staging/


# Set up the convert.json script fileSetSize to 1 (to be used for converting
# each binary file singularly
echo "copying convert.json to mod.json"
cp $CONVERTSRCDIR/convert.json $CONVERTSRCDIR/mod.json
echo "replacing existing fileSetSize with a value of 1:"
sed -r 's/"fileSetSize":.*[0-9]+, /"fileSetSize":1,/g' $CONVERTSRCDIR/mod.json > $CONVERTSRCDIR/new.json

#echo "Invoke python script for stitching FastEddy binary files"
#python_cmd=/Volumes/d1/minnawin/miniforge3/envs/fasteddy_env/bin/python
#echo "running with $python_cmd"
#
#
#condition='True'
#while [ $condition = 'True' ]; do
#   echo "condition = $condition"
#   for (( i=0; i<2; i++)); do
#     if [ -f "$CONVERTSRCDIR/FEstitcher.py" ]; then
#        $python_cmd $CONVERTSRCDIR/FEstitcher.py
#        if [ $i = 1 ]; then
#          echo "i is $i, setting condition to 1"
#          condition=1
#          break
#        fi
#     else
#         echo "$CONVERTSRCDIR/FEstitcher.py does not exist."
#         condition='False'
#         break
#     fi
#   done
#done
#echo "outside of while"
