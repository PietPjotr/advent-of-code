#!/bin/bash
# A simple variable example

VAR1="Hello, "
VAR2="${VAR1}World"

pythonfile="dag${1}.py"

inputdir="inputs/"
inputfile="${inputdir}dag${1}.txt"
testfile="${inputdir}dag${1}_test.txt"

for file in $pythonfile $inputfile $testfile
do
#  echo "Creating $file"
if [ ! -f $file ]
then
    touch $file
fi
done
