#!/bin/bash
if getent passwd $1 > /dev/null 2>$1; then
echo "Yes the user exists"
else
echo "User does not exist."
fi
