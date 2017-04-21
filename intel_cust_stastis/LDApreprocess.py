# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:59:47 2017

@author: changlue.she
"""
import jieba.posseg as pseg
import jieba
import pandas as pd
 
jieba.load_userdict('../intel_cust_stastis/userDict.txt')  
#---------------------------------------------------------------------------------------------------
rawdata = pd.read_csv('../../TFProj/Natural language process/corpus/opr_rem.csv',
                      header=0)
rawdata = rawdata.drop_duplicates()
#---------------------------------------------------------------------------------------------------
corpus = []
sentences = []
userIDs = range(len(rawdata['opr_rem']))
conversations = list(rawdata[u'opr_rem'])

for sentence in conversations:
    sentence = str(sentence)
    sentence = sentence.replace('\t','')
    words = [pair.word for pair in pseg.lcut(sentence) if pair.flag in ['n','ns','vs','nv']]       
    if len(words)>2:
         corpus.append(words)
         sentences.append(sentence)
 