#!/bin/bash
echo "Enter two numbers:"
read x
read y
if [ $x -eq $y ]; then
echo "They are equal"
else
echo "They are not equal"
fi
