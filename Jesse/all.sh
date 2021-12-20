#!/bin/bash

start=$SECONDS
NUM=$(ls -l ./ | grep -c ^d)
for i in $(seq 1 $NUM); do 
    echo Day $i
    cd Day_$i
    python main.py
    echo
    cd ../
done
echo $(( SECONDS - start )) seconds to finish