# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:59:47 2017

@author: changlue.she
"""
import jieba.posseg as pseg
import jieba
import pandas as pd
 
jieba.load_userdict('C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/pythonProj/intel_cust_stastis/userDict.txt')  
#---------------------------------------------------------------------------------------------------
rawdata = pd.read_csv('C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/MSXF/message feature etl/smsResult.csv',
                      header=0,encoding='gbk' )
rawdata = rawdata.drop_duplicates()
#---------------------------------------------------------------------------------------------------
corpus = []
sentences = []
userIDs = range(len(rawdata['x']))
conversations = list(rawdata[u'x'])

for sentence in conversations:
    sentence = sentence.replace('\t','')
    words = [pair.word for pair in pseg.lcut(sentence) if pair.flag in ['n','ns','vs','nv']]       
    if len(words)>2:
         corpus.append(words)
         sentences.append(sentence)
 