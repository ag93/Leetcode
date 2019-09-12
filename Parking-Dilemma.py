#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'carParkingRoof' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY cars
#  2. INTEGER k
#

def carParkingRoof(cars, k):
    # Write your code here
    cars = sorted(cars)
    roof_len = []
    left = 0
    right = k-1
    while(right<len(cars)):
        roof_len.append(cars[right] - cars[left]+1)
        left = left+1
        right = right+1
    return(min(roof_len))
if __name__ == '__main__':