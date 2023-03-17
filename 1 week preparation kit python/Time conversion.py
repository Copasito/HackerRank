#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    hour, minute, temp = s.split(':')
    second, period = temp[0:2], temp[2:4]
    
    hour = int(hour)
    
    if period == 'AM':
        if hour == 12:
            hour = hour - hour
        
    elif period == 'PM':
        if hour != 12:
            hour = hour + 12
    
    return '{:0>2}:{:0>2}:{:0>2}'.format(hour, minute, second)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
