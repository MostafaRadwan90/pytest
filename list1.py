#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:27:06 2022

@author: mo
"""

if __name__ == '__main__':
    order={}
    list1=[]
    list2=[]
    list3=[]
    N = int(input())
    for i in range(N):
        command, *line = input().split()
        #print(command)
        numbers = list(map(float, line))
        list1.append(command)
        list2.append(numbers)
    print(list1)
    print("\n")
    print(list2)
    #print("\n")
    #print(numbers)
    #if bool(list2[3]):
    #   print("yes")
    for t in range (N):
        if (list1[t]!='print' ):
            command1=list1[t]
            print(command1)
            list3.command1(list2[t])
         