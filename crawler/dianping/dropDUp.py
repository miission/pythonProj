# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 16:55:23 2017

@author: changlue.she
"""
import pandas as pd
for firstClassIdx in [0,1,2,3,4,8,9,11,12,13,14,15,16]:
  
    foodTypes = allTypes[firstClassIdx].findAll('a')
 
    firstClassName = foodTypes[0].text
     
    #------------------------------------------------------------------------------
    '''pick save and load the brands'''
    dirs = "C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\Python\\NLP\\savedObject\\meituan\\"
    dirs = dirs+firstClassName+'.pkl'
 
    allClassLoads = cPickle.load(open(dirs,"rb"))
    #------------------------------------------------------------------------------
    '''save the brands into csv'''
    BrandDF = pd.DataFrame(allClassLoads,columns=[u'所属分类',u'店面招牌',u'是否广告',u'优惠措施',u'评级等级',u'评价数量',u'平均消费',u'店面地址',u'未知字段1',u'未知字段2',u'未知字段3'])
    BrandDF = BrandDF.drop_duplicates()     
    dirs = 'C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\MSXF\\feature construct\\doc\\meituan\\'
    dirs = dirs+firstClassName+'.csv'
    BrandDF.to_csv(dirs,encoding='gb18030',index=False,columns=[u'所属分类',u'店面招牌',u'是否广告',u'优惠措施',u'评级等级',u'评价数量',u'平均消费',u'店面地址',u'未知字段1',u'未知字段2',u'未知字段3'])
     