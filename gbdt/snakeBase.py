# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:20:01 2016

@author: changlue.she
"""
from __future__ import division
import numpy as np
from sklearn.linear_model  import   Ridge 
class sreg():
    def __init__(self,depth=5):
        self.depth = depth

    def fit(self,x,y):  
        y[y==-1]=0
        self.fidx = np.random.choice(x.shape[1],2,replace=False)  
        xx = x.T[self.fidx].T
        self.reg = Ridge (alpha = .1)
        self.reg.fit(xx,y) 
        return self,self.reg.predict(xx)
        
    def predict(self,x):
        xx = x.T[self.fidx].T
        return self.reg.predict(xx)