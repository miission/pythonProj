# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:32:45 2017

@author: changlue.she
"""
import pandas as pd
file = 'C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/MSXF/intel_cust/statistics/rawdatas/details/201701m/马上消费金融_changlue.she_2017-01-'

for i in range(1,32):
    if i==1:
        init=True
    else:
        init = False
    i = str(i)
    if len(i)==1:
        i="0"+i
    filei = file+i+".csv"
    tmp = pd.read_csv(filei,header=0,encoding='gbk',usecols=[u'消息目标',u'会话Id',u'消息内容'])
    if init:
        rawdata = tmp
    else:
        rawdata = pd.concat([rawdata,tmp])  
 
rawdata = rawdata.dropna()
