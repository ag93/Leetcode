#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'finalInstances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER instances
#  2. INTEGER_ARRAY averageUtil
#
import math
def finalInstances(instances, averageUtil):
    # Write your code here
    
    left = 0
    
    while(left < len(averageUtil)):

        current = averageUtil[left]
        if current >= 25 and current <= 60:
            left = left + 1

        elif(current < 25):
            if(instances>1):
                instances = instances/2
                instances = math.ceil(instances)
                left = left+11
            else:
                left = left + 1
        else:
            temp = instances*2
            if temp < (2*(10**8)):
                instances = temp
                left = left+11
            else:
                left = left + 1    
    return(instances)

if __name__ == '__main__':