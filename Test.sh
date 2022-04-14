#!/bin/bash

FILEPATH='/home/ec2-user/environment/Python_Scripts/PythonScripts/testdir/'

echo $FILEPATH

if [ -d $FILEPATH ]
then
echo $FILEPATH
for (( i=0; i<10; i++ ))
do
touch file$i
done
for f in file*
do
echo "test" > $f
done
fi