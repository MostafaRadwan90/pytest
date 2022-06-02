#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:58:52 2022

@author: mo
"""

if __name__ == '__main__':
    average=0
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
len1= len(student_marks[query_name])
for i in range(len1):
    average=average+student_marks[query_name][i]/len1   
print("%.2f"% average)    