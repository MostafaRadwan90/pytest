#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 10:51:47 2022

@author: mo
"""
# n=2
# arr=[[1,2],[8,9]]
# print(arr[0][0],arr[0][1],arr[1][0],arr[1][1]) 
# for kk in range (2):
#     print(arr[n-kk-1][kk])

#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    primary=0
    secondery=0
    result=0   
    for i in range (n):
      primary+=arr[i][i]
      #print(primary)  
    #bar=(n-1,-1,-1) 
    #foo=(0,n,1) 
    #for t,j in zip (bar,foo):
    #secondery+=arr[t][j]
    for kk in range(n):
        secondery+=arr[n-kk-1][kk]
        #print(arr[2][0],arr[1][1],arr[0][2])
    result=abs(primary-secondery)    
    return(result)  
if __name__ == '__main__':
    fptr = open('/home/mo/Desktop/pytest/diagonal.txt', 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
