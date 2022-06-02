#!/usr/bin/env python3
# -*- coding: utf-8 -*-
4"""
Created on Thu Apr 21 15:21:57 2022

@author: mo
"""

if __name__ == '__main__':
    n = int(input())
    flag=0
    arr = map(int, input().split())
    t=list(arr)
    list1 = [int(x) for x in t]
    list1.sort()
    #print(list1)
    for i in range(n-1,-1,-1):
        if (list1[i]!=list1[i-1] and flag==0):
            print(list1[i-1])
          #  print(" here is flag befor ",flag)
            flag=1
           # print(" here is flag after ",flag)

# =============================================================================
#         print(list1)
#         print("here is i value ",i)
#         print("here is 1 ",list1[i])
#         print("here is 2 ",list1[i-1])
# =============================================================================
       # while (list1[i]>list1[i-1]):
        # print(list1[i-1])
         #break