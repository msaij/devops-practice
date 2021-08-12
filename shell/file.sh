#!/bin/bash
fn=$1
if [[ -f "$fn" ]]; then
echo "yes"
else
echo "no"
fi
