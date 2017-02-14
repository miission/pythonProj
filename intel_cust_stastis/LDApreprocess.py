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
#rawdata = pd.read_csv('C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/MSXF/intel_cust/statistics/history/conversation.csv',
#                      header=0,encoding='gbk',usecols=[u'消息目标',u'会话ID',u'消息内容'])
rawdata = rawdata.loc[rawdata[u'消息目标'] == u'机器人',:]    
rawdata = rawdata.sort([u'会话Id'])
rawdata = rawdata.drop_duplicates()
#---------------------------------------------------------------------------------------------------
corpus = []
sentences = []
userIDs = list(rawdata[u'会话Id'])
conversations = list(rawdata[u'消息内容'])
for sentence in conversations:
    sentence = sentence.replace('\t','')
    words = [pair.word for pair in pseg.lcut(sentence) if pair.flag in ['n','ns','vs','nv']]       
    if len(words)>2:
         corpus.append(words)
         sentences.append(sentence)
 