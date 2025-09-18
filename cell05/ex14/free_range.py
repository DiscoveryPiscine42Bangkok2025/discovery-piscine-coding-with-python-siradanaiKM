#!/usr/bin/env python3
import sys

if(len(sys.argv) != 3):
    print("none")

first = int(sys.argv[1])
last = int(sys.argv[2])

arr = []
for i in range(first,last+1):
    arr.append(i)

print(arr)