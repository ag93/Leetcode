#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY numbers
#
from collections import Counter
def solve(k, numbers):
    # Write your code here
    if(len(numbers) == 0 or not numbers):
        return("No")

    if len(numbers)%k == 0: 
        temp = Counter(numbers)
        max_rep = max(temp.values())
        if (max_rep > (len(numbers)/k)):
            return("No")
        else:
            return("Yes")

    else:
        return("No")

if __name__ == '__main__':