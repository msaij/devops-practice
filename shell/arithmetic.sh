#!/bin/bash
echo "Enter first number"
read x
echo "Enter second number"
read y
echo "1.sum 2.sub 3.mul"
echo "Pick your operation"
read o
if [ $o -eq 1 ];
then
(( sum=x+y ))
echo "The sum is: $sum"
elif [ $o -eq 2 ];
then
(( sub=x-y ))
echo "The sub is: $sub"
elif [ $o -eq 3 ];
then
(( mul=x*y ))
echo "The mul is: $mul"
else
echo "You have not picked your option properly"
fi
