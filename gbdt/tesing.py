# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 10:23:03 2016

@author: changlue.she
"""
import numpy as np
import numba
import datetime
from numba import vectorize,int32
def ff(x,y):   
    return x+y
    
    
@vectorize([int32(int32, int32)])
def f(x,y):
    return x+y

x= np.arange(100000000) 
y= np.arange(100000000) 
a = datetime.datetime.now()
s1 = f(x,y)
b = datetime.datetime.now()
print b-a
a = datetime.datetime.now()
s2 = ff(x,y)
b = datetime.datetime.now()
print b-a
np.where(s1!=s2)


a = datetime.datetime.now()
mp1 = np.where(x<10000)
y = x[mp1]
b = datetime.datetime.now()
print b-a
a =np.array([True,False])
np.invert(a)
~a
a = datetime.datetime.now()
mp2 = x<10000
y = x[mp2]
b = datetime.datetime.now()
print b-a

a = datetime.datetime.now()
mp3 = f(x,10000)
y = x[mp3]
b = datetime.datetime.now()
print b-a
 