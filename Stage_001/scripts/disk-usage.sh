#!/bin/bash

threshold=80
logfile="$HOME/disk-check.log"

usage=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')

if [ "$usage" -gt "$threshold" ]; then
    echo "$(date): WARNING - Disk usage at ${usage}% (threshold: ${threshold}%)" >> "$logfile"
else
    echo "$(date): OK - Disk usage at ${usage}%" >> "$logfile"
fi
