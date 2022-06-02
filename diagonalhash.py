#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:18:18 2022

@author: mo
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code
    k=0
    while(k<n):
     for i in range (k,n-1):
       print(" ",end="")
     for j in range(0,k+1,1):
        print("#",end="")
     print('\n')
     k+=1
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
