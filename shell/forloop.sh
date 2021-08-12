#!/bin/bash
echo "Enter the number upto whcih you want to print the sequence:"
read n
for (( i=0; i<=$n; i++ ))
do
echo "$i"
done
