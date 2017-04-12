# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:59:47 2017

@author: changlue.she
"""
import jieba.posseg as pseg
import jieba
import pandas as pd
import numpy as np
from collections import Counter
jieba.load_userdict('C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/pythonProj/intel_cust_stastis/userDict.txt')  
#---------------------------------------------------------------------------------------------------
#rawdata = pd.read_csv('C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/MSXF/ZhiChi/Statistic/output/conversation.csv',
#                      header=0,encoding='gbk',usecols=[u'消息目标',u'会话ID',u'消息内容'])
#rawdata = rawdata.loc[rawdata[u'消息目标'] == u'机器人',:]    
#rawdata = rawdata.sort([u'会话ID'])

rawdata = pd.read_csv('C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/MSXF/message feature etl/smsResult.csv',
                      header=0,encoding='gbk' )
rawdata = rawdata.drop_duplicates()
#---------------------------------------------------------------------------------------------------
TF_term = []
IDF_term = []
ALL_term = []
#userIDs = list(rawdata[u'会话ID'])
userIDs = range(len(rawdata['x']))
conversations = list(rawdata[u'x'])
oldidx=None
add = ['used to drop']
 
for idx,userID in enumerate(userIDs):
    conversation = conversations[idx]
    if  len(conversation)>6:
        conversation = [pair.word for pair in pseg.lcut(conversation) if pair.flag in ['n','ns','vs','nv']]       
        if len(conversation)>0:
            if userID!=oldidx:
                 oldidx = userID
                 ALL_term += add
                 tf = dict(Counter(add))
                 IDF_term+=tf.keys()
                 TF_term.append(tf)
                 add = conversation
            else:
                 add+= conversation
                 
TF_term.pop(0)             
wordFreq  = dict(Counter(ALL_term))
allDocNum = len(TF_term)
IDF       = dict(Counter(IDF_term))
keyWord   = []
tfidf     = []
for tf in TF_term:
    tmp = 0
    for word in tf.keys():
        tf_idf = tf[word]*np.log(allDocNum/IDF[word])
        if tf_idf>tmp:
            tmp  = tf_idf
            keyW = word
            tfs  = tf_idf
        keyWord.append(keyW)
        tfidf.append(tfs)
        tmp = 0
keyWord = dict(Counter(keyWord))        

idxs = np.argsort(-np.array(list(keyWord.values())))[:20]
keywords = [list(keyWord.keys())[idx] for idx in idxs]
wordFreq = [wordFreq[word] for word in keywords]
#save those key words
outfile = pd.DataFrame([keywords,wordFreq])
outfile = outfile.T
dirs = 'C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/MSXF/message feature etl/关键词句.xlsx'
outfile.to_excel(dirs,encoding='gb18030',index=False )
 