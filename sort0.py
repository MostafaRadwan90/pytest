#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:57:04 2022

@author: mo
"""
# =============================================================================
# # =============================================================================
# # 
   if __name__ == '__main__':
     n = int(input())
     arr = map(int, input().split())
     t=list(arr)
     list1 = [int(x) for x in t]
     list1.sort()
     print(list1)
     print(list1[n-1])
# =============================================================================
#   
#     if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     t=list(arr)
#     list1 = [int(x) for x in t]
#     list1.sort()
#    # print(list1)
#     for i in range(n,0,-1): 
#         print(list1)
#         print("here is 1 "+list1[i])
#         print("here is 2 "+list1[i-1])
#        # while (list1[i]>list1[i-1]):
#         # print(list1[i-1])
#          #break
# =============================================================================
