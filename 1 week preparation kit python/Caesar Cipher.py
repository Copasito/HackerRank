#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k, n):
    # Write your code here
    #ord() returns the unicode of a char
    ans = ""
    for i in range(n):
        oLetter = ord(s[i])
        #print(oLetter)
        if (oLetter >= 97 and oLetter <= 122) :
            letter = oLetter + k
            if letter > 122:
                letter -= 26
            ans += chr(letter)
                
        elif (oLetter >= 65 and oLetter <= 90) :
            letter = oLetter + k
            if letter > 90:
                letter -= 26
            ans += chr(letter)
        else:
            ans+=s[i]
    return ans;
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k, n)

    fptr.write(result + '\n')

    fptr.close()
