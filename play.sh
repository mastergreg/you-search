#!/bin/bash
while read line
do
    youtube.sh $line
done < $1
