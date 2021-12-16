#!/bin/bash

for d in */ ; do
    echo "$d"
    cd "$d"
    python main.py
    echo
    cd ../
done