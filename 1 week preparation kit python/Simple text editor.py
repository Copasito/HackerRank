# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys
def editor(q, queries):
    ans = []
    stack = []
    buff = ""
    buff = [*buff]
    for i in range(q):
        op = int(queries[i][0]) #the operation we have to make
        if op == 1: #add queries[i][1] to the text
            stack.append(buff) 
            buff += queries[i][1]
        if op == 2: #delete last k characters of the text
            stack.append(buff) 
            k = int(queries[i][1])
            buff = buff[:-k]
        if op == 3: #print the kth character
            k = int(queries[i][1])
            #print(buff[k])
            ans.append(buff[k - 1])
        if op == 4: #undo a operation
            buff = stack.pop()
        
        
    
    return ans;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    
    for i in range(q):
        querie = input().split()
        queries.append(querie)

    result = editor(q, queries)
    
    for i in range(len(result)):       
        fptr.write(str(result[i]) + '\n')

    fptr.close()
