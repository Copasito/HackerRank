#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr, n):
    # Write your code here
    frec = [0 for i in range(100)]
    i = 0
    
    while i < n:
        frec[arr[i]] += 1
        i += 1
    
    return frec;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr,n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
