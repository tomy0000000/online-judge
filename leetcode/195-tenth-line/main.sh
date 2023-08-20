#!/bin/bash

t="${t:-1}"
while IFS= read -r line; do
    if [ "$t" = 10 ]; then
        echo "$line"
    fi
    t=$((t + 1))
done <file.txt
if [ "$t" = 10 ]; then
    echo "$line"
fi
