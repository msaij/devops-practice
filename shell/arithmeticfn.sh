#!/bin/bash

perform() {
a=$1
b=$2
o=$3

if [[ $o == "sum" ]]; then
r=$((a+b))
echo "sum is $r"

elif [[ $o == "sub" ]]; then
r=$((a-b))
echo "sub is $r"

elif [[ $o == "mul" ]]; then
r=$((a*b))
echo "mul is $r"

else
echo "Enter the input properly."

fi
}
perform $1 $2 $3
