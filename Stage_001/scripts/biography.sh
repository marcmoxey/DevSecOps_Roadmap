#!/bin/bash 


job=$1

# ask user for age
 read -p "Enter your age: " age

# check if there under 18
    # if under 18
        # print "not eligible for work"
    # else 18+
        # use read again  to  ask for their job
if [ "$age" -lt 18 ]; then
    echo "not eligible for work"
else 
    read -p "What is your job: " job
fi
