# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys

#Queue taken from https://www.geeksforgeeks.org/queue-using-stacks/
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
  
    # EnQueue item to the queue
    def enQueue(self, x):
        self.s1.append(x)
  
    # DeQueue item from the queue
    def deQueue(self):
  
        # if both the stacks are empty
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Q is Empty")
            return
  
        # if s2 is empty and s1 has elements
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
  
        else:
            return self.s2.pop()
    
    def front(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Q is Empty")
            return
        
        # if s2 is empty and s1 has elements
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2[-1]
  
        else:
            return self.s2[-1]
        
        
        
def operation(q, queries):
    ans = [] #a list with the values to print
    temp = Queue()
    
    for i in range(q):
        op = queries[i][0] #the operation we have to make
        if op == 1:
            temp.enQueue(queries[i][1])
        elif op == 2:
            temp.deQueue()
        else:
            ans.append(temp.front())
            
    return ans;
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    
    for i in range(q):
        querie = list(map(int, input().split()))
        queries.append(querie)

    result = operation(q, queries)
    
    for i in range(len(result)):       
        fptr.write(str(result[i]) + '\n')

    fptr.close()
