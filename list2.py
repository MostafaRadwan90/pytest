#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 17:04:43 2022

@author: mo
"""

if __name__ == '__main__':
    N = int(input())
    arr = []
    n1 = 0;
    n2 = 0;
    for x in range(N):
        comand = input()
        #print(comand)
        comand = comand.split()
        #print(comand)
        if comand[0] == "insert":
            n1 = int(comand[1])
            n2 = int(comand[2])
            arr.insert(n1,n2)
        elif comand[0] == "print":
            print(arr)
        elif comand[0] == "remove":
            n1 = int(comand[1])
            arr.remove(n1)
        elif comand[0] == "append":
            n1 = int(comand[1])
            arr.append(n1)
        elif comand[0] == "sort":
            arr.sort()
        elif comand[0] == "pop":
            arr.pop()
        elif comand[0] == "reverse":
            arr.reverse()