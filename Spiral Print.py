# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:56:18 2019

@author: anike
"""
# Python3 program to print  
# given matrix in spiral form 
def spiralPrint(m, n, a) : 
    k = 0; l = 0
    result = []
    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''
        
    while (k < m and l < n) :           
        # Print the first row from 
        # the remaining rows  
        for i in range(l, n) :
            result.append(a[k][i])
        k += 1
  
        # Print the last column from 
        # the remaining columns  
        for i in range(k, m) :
            result.append(a[i][n - 1])           
        n -= 1
        
        # Print the last row from 
        # the remaining rows  
        if (k < m) : 
            for i in range(n - 1, (l - 1), -1) :
                result.append(a[m - 1][i])
            m -= 1
          
        # Print the first column from 
        # the remaining columns  
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) :   
                result.append(a[i][l])
              
            l += 1
    return (result)
  
# Driver Code 
a = [ [7,7,3,8,1], 
      [13,5,4,5,2], 
      [9,2,12,3,9],
      [6,12,1,11,41]] 
        
R = len(a); C = len(a[0])
temp = spiralPrint(R, C, a) 
print(temp)
