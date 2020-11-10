#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    visited = [False] * len(arr)
    swap = 0
    i = 0
    
    while not all(visited):
        visited[i] = True
        if i + 1 != arr[i]:
            if not visited[arr[i] - 1]:
                swap += 1
                i = arr[i] - 1
                continue
            elif False in visited:
                i = visited.index(False)
                continue
        i += 1
                    
    return swap

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

