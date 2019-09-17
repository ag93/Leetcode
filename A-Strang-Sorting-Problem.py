# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:17:22 2019

@author: anike
"""

mapping = [3,5,4,6,2,7,9,8,0,1]

nums = ['990','332','32']
new_nums = []


for number in nums:
    temp = ""
    for i in range(len(number)):
        temp += str(mapping.index(int(number[i])))
    new_nums.append(temp)
    
mapped = dict(zip(new_nums, nums))

new_nums = sorted(new_nums)

result = []
for item in new_nums:
    result.append(mapped[item])

print(result)