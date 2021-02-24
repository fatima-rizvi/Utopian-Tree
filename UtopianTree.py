#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    # Create a counter to keep track of what cycle we're on
    # If the counter is odd, increase the height by one
    # If the counter is even, double the height
    
    cycle_count = 1
    height = 1
    
    if n == 0:
        return height
    
    while cycle_count <= n:
        if cycle_count % 2 == 0:
            height += 1
        else:
            height = height * 2
        # print(f"P: {cycle_count}, H: {height}")
            
        cycle_count += 1
    
    return height
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
