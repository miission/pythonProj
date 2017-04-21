# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 11:22:35 2016

@author: changlue.she
"""
from __future__ import division
import numpy as np
from NeuronLayers.activeFunctions import actfuncs
from NeuronLayers.BasicNeuron import softmaxLayer
#import pickle
from intel_cust_stastis.LDApreprocess import corpus,sentences
#-----------------------------------------------------------------------------------------------------------------------------------------------
#corps = pickle.load(open("C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\pick1214sec.pkl","rb"))
wordCorps = corpus
#for idx in corps:
#    corp = []
#    for diag in corps[idx]:
#        corp+=diag
#    wordCorps.append([w for w in corp])
wordDict = {}
for corp in wordCorps:
    for w in corp:
        wordDict.setdefault(w,0)
        wordDict[w]+=1       
word2code = {}
code2word = []
idx=0
for w in wordDict:
    if wordDict[w]>3:
        if w not in word2code:
            word2code[w] = idx
            idx+=1
            code2word.append(w)
wordCorp = []
for corp in wordCorps:
    if len(corp)>2:      
        wordCorp.append([w for w in corp if w in word2code])
wordCorps = []
codeCorps = []
for corp in wordCorp:       
    wordCorps.append(corp)
    codeCorps.append([word2code[w]for w in list(set(corp))])
#-----------------------------------------------------------------------------------------------------------------------------------------------
topicNums = 8
docNums = len(codeCorps)
wordNums = len(code2word)
doc2topic = np.random.normal(size = (docNums,topicNums)) 
word2topic = np.random.normal(size = (wordNums,topicNums))
topicSoft = softmaxLayer()
wordSoft = softmaxLayer()
#-----------------------------------------------------------------------------------------------------------------------------------------------
word2doc = np.zeros(shape=(docNums,wordNums))
for docidx in range(docNums):
    doc = codeCorps[docidx]
    word2doc[docidx][doc]=1
word2doc = word2doc.T
#-----------------------------------------------------------------------------------------------------------------------------------------------
learning =0.001
l2 = 0
ers = 0
cot = 0
ccot= 0
best = 1
while 2>1:
    if ccot>5:
        break   
    wordMixtrue  = wordSoft.actNuerous(word2topic)
    topicMixtrue = topicSoft.actNuerous(doc2topic)
    pred,tmp     = actfuncs.softmax(wordMixtrue.dot(topicMixtrue.T))
    
    error        = pred*np.array([np.sum(word2doc,axis=1)]).T-word2doc
    ers         += np.mean(np.abs(error))
    cot+=1
    if cot>=100:
        ers     /= cot
        print (ers)
        ccot    +=1
        if ers<best:
            best = ers
            ccot = 0
        cot=0
        ers=0
    error          *= np.array([np.sum(word2doc,axis=1)]).T
    doc2topicError  = topicSoft.updateError((wordMixtrue.T.dot(error)).T)
    word2topicError = wordSoft.updateError(error.dot(topicMixtrue))
    doc2topic      -= (doc2topicError*learning+doc2topic*l2)
    word2topic     -= (word2topicError*learning+word2topic*l2)
#-----------------------------------------------------------------------------------------------------------------------------------------------
outDF = []
keywords = []
keysentences = []
for idx in range(topicNums):    
    word2topicSoft =  wordSoft.actNuerous(word2topic)
    ords = np.argsort(-word2topicSoft.T[idx])[:10]
    tmp = ['主题'+str(idx+1),'主题关键词']
    tmp += [code2word[i]for i in ords]
    keywords+=tmp
    topic2docSoft = topicSoft.actNuerous(doc2topic)
    ords = np.argsort(-topic2docSoft.T[idx])[:10]
    tmp = ['','主题关键句']
    tmp +=[sentences[i]for i in ords]
    keysentences+=tmp
outDF = [keywords,keysentences]   
import pandas as pd
outDF = pd.DataFrame(outDF)
outDF = outDF.T
dirs = '../../MSXF/message feature etl/主题词句.xlsx'
outDF.to_excel(dirs,encoding='gb18030',index=False,header=None )
