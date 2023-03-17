#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    # Write your code here
    
    ans = 0
    #sumo la diagonal \
    i = 0
    LtoR = 0
    RtoL = 0
    while i < n:
        j = i + 1
        LtoR += arr[i][i]
        RtoL += arr[i][-j]
        i += 1
    #print(LtoR)
    #print(RtoL)
    ans = abs(LtoR - RtoL)
    return ans;
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
