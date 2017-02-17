# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:08:07 2017

@author: changlue.she
"""
 
fl=open('C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/CPlusPractice/word2vecPC/word2vecPC/brown.txt', 'w')
for sentence in corps:
    fl.write(" ".join(sentence))
    fl.write("\n")
fl.close()
 