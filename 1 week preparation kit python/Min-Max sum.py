#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    n = 5
    ans = []
    mins = 0
    mintemp = arr[0]
    maxs = 0
    maxtemp = arr[0]
    """
    for i in range(5):
        mins.append(arr[i])
        maxs.append(arr[i])
        if arr[i] < mintemp:
            mintemp = arr[i]
        if arr[i] > maxtemp:
            maxtemp = arr[i]
    #elimino solo al mayor/menor elemento de cada arreglo
            """
    
    for i in range(5):
        maxs = maxs + arr[i]
        mins = mins + arr[i]
        if arr[i] < mintemp:
            mintemp = arr[i]
        if arr[i] > maxtemp:
            maxtemp = arr[i]
    
    maxs = maxs - mintemp
    mins = mins - maxtemp
    
    ans.append(mins)
    ans.append(maxs)
    
    # en lugar de guardar en un arreglo los valores, mejor haz una suma y luego sustraes el elemento que no entra
    return ans

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    ans = miniMaxSum(arr)
    
    print(str(ans[0]) + " " + str(ans[1]))
