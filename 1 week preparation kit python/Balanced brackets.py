#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    s1 = []
    s = [*s]
    i = 0
    redF = True
    ans = "YES"
    while i < len(s):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            s1.append(s[i])
        else:
            if len(s1) > 0:
                temp = s1.pop()
                if s[i] == ')' and temp != '(':
                    ans = "NO"
                elif s[i] == ']' and temp != '[':
                    ans = "NO"
                elif s[i] == '}' and temp != '{':
                    ans = "NO"
            else:
                ans = "NO"
        i += 1    
    return ans;
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input().strip()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
