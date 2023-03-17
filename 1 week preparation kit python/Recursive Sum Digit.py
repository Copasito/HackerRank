#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def sumDigits(n):
    n = sum(list(map(int,[*str(n)])))
    return n;

def recursiveDigits(n):
    if n % 10 == n:
        return n
    else:
        n = sumDigits(n)
        return recursiveDigits(n) ;

def superDigit(n,k):
    n = sumDigits(n)
    n *= k
    return recursiveDigits(n) ;
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
