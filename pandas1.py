#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:01:07 2022

@author: mo
"""

import pandas as pd
import numpy as np
from numpy.random import rand
#np.random.seed(2312311612)
headers=['name', 'age', 'weight']
values=['a', 28, 90]
myser=pd.Series(data=values, index=headers)
print(myser)
mysecser=pd.Series(values)
print(mysecser)
sem1= pd.Series(data=['54', '234'], index=['math', 'phy'])
sem2= pd.Series(data=['500', '934'], index=['Cs', 'ESC'])

print(sem1,"\n",sem2)
print(sem1+sem2)
df1=pd.DataFrame(index=['x','y'] ,columns=['c1','c2'])
print(df1)
print(np.random.randn(5,5))
df5=pd.DataFrame(np.round(np.random.randn(2,5)),index=['x','y'] ,columns=['c1','c2','c3','c4','c5'])
print(df5)
print(df5['c4'])