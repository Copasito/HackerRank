#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid, n):
    # Write your code here
    ans = "YES"
    rows = []
    maxRows = []
    minRows = []
    
    for i in range(n):
        rowSum = 0
        
        minRows.append( ord( grid[i][0] ) )
        maxRows.append( ord( grid[i][0] ) )
        
        
        for j in range( len(grid[i]) ):
            rowSum += ord( grid[i][j] )
            
            if ord( grid[i][j] ) < minRows[i]:
                minRows[i] = ord( grid[i][j] )
            if ord( grid[i][j] ) > maxRows[i]:
                maxRows[i] = ord( grid[i][j] )
            
                
        rows.append(rowSum)
    
    for i in range(n-1):
        
        if rows[i] > rows[i+1]:
            ans = "NO"
        
        if maxRows[i] > maxRows[i+1]:
            ans = "NO"
        if minRows[i] > minRows[i+1]:
            ans = "NO"
        
    return ans;
        
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid, n)

        fptr.write(result + '\n')

    fptr.close()
