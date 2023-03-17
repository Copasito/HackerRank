#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr, n):
    ans = []
    plus = 0
    minus = 0
    zero = 0
    
    for i in range(n):
        if arr[i] > 0:
            plus += 1
        elif arr[i] < 0:
            minus += 1
        elif arr[i] == 0:
            zero += 1
            
    ans.append(plus/n)
    ans.append(minus/n)
    ans.append(zero/n)
    
    
    return ans;
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    ans = plusMinus(arr, n)
    
    for i in range(3):
        print(round(ans[i], 6))
    
    