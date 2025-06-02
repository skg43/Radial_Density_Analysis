#!/bin/sh

# run.sh
# 
# This script runs the NTF2 flux analysis pipeline.
# It sets up the environment, executes the Python analysis, and handles output management.

{
TIME=`date`
echo " "
liner=`echo "     +++++++++++++++++++++++++++++++++++++++++++++++++++++++"`
echo $liner
echo " "
echo "                     Redial Density Calculation       "
echo " "
echo "                  All Rights Reserved  "
echo " "
echo "        developed by: Sanjeev Kumar Gautam "
echo " "
echo $liner
echo " "
echo " Date: $TIME  "
echo " "

# remove .txt files from old run
for file in *.txt; do
    if [ -f $file ]; then
		echo " ... removing $file in 'run' directory"
		rm -f $file
    fi
done

cd ../src

# run the python code to generate new .data files
my_code="run.py"
if [ -f $my_code ]; then
	echo " "
	echo " ... running run.py"
	python3 run.py
	echo " "
else
	echo " "
	echo "***error: can't find run.py file"
fi

# transfer .txt files into ../run folder
for file in *.txt; do
    if [ -f $file ]; then
		echo " ... moving $file to 'run' directory"
		mv $file ../run
    fi
done
echo " "
} > run.log
