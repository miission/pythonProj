# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:21:07 2016

@author: changlue.she
"""
 
import urllib2
from bs4 import BeautifulSoup
import cPickle
import pandas as pd
import re
'''get the first class categories'''
url = 'https://www.dianping.com/search/category/2/10/g110r1465'
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent
req=urllib2.Request(url,headers=header)
response=BeautifulSoup(urllib2.urlopen(req,None))
p = re.compile(r'\d+')
'''get all the stuffs that sale'''
allTypes = response.find('ul').findAll('li')
'''get food category of sales'''
for firstClassIdx in [7]:
    allFoodList = [] 
    foodTypes = allTypes[firstClassIdx].findAll('a')
    idx = 0
    firstClassName = foodTypes[0].text
    crawledURL = []
    '''get subCategories's title'''
    for foodType in foodTypes[1:]:
        subFoodTypeName = foodType.text
        subFoodTypeUrl  = foodType['href']
        if subFoodTypeUrl in crawledURL:
            next
        else:
            crawledURL.append(subFoodTypeUrl)
        while(subFoodTypeUrl!='None'):
            try:                
                foodReq=urllib2.Request(subFoodTypeUrl,headers=header)
                foodResponse=BeautifulSoup(urllib2.urlopen(foodReq,None))         
                subFoodTypeUrl = 'http://www.dianping.com'+ foodResponse.find('div',{'class':'page'}).find('a',{'class':'next'})['href']          
            except:
                subFoodTypeUrl = 'None'
            try:    
                foodContents = foodResponse.find('div',{'class':'shop-wrap'}).findAll('li')
            except:
                next
            for foodContent in foodContents:  
                idx+=1 
                if idx%1000==0:
                    print firstClassName
                foddDetail = foodContent.find('div',{'class':'info'})
                '''get titles'''
                try:
                   brand = foddDetail.find('p',{'class':'title'}).find('a').text.replace('\n','') 
                except:
                    next
                try:
                    promoSlogns = foddDetail.find('div',{'class':'more-info'}).findAll('a')
                    promoSlogn = '###'.join([promoSlogn.find('span')['title'] for promoSlogn in promoSlogns])
                except:
                    promoSlogn = -1
                '''get comments'''
                try:
                    comments = foddDetail.find('p',{'class':'remark'}).findAll('span') 
                    rate = [-1,-1,-1]
                    for idx,value in enumerate(comments):
                        if idx ==0:
                            try:
                                rate[idx] = comments[idx]['title']
                            except:
                                rate[idx] = -1
                        else:
                            try:
                                rate[idx] = p.findall(comments[idx].text)[0]   
                            except:
                                rate[idx] = -1
                except:
                    rate = [-1,-1,-1]
                try:
                    address = foddDetail.find('p',{'class':'area-key'}).text.replace('\n','').replace(' ','')
                except:
                    address = -1
           
                allFoodList.append([subFoodTypeName,brand,promoSlogn,address]+rate)
                 
    #------------------------------------------------------------------------------
    '''pick save and load the brands'''
    dirs = "C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\Python\\NLP\\savedObject\\meituan\\"
    dirs = dirs+firstClassName+'.pkl'
    cPickle.dump(allFoodList,open(dirs,"wb")) 
    allClassLoads = cPickle.load(open(dirs,"rb"))
    #------------------------------------------------------------------------------
    '''save the brands into csv'''
    BrandDF = pd.DataFrame(allFoodList,columns=[u'所属分类',u'店面招牌',u'优惠措施',u'店面地址',u'评价等级',u'评价数量',u'平均消费'])
    dirs = 'C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\MSXF\\feature construct\\doc\\meituan\\'
    dirs = dirs+firstClassName+'.csv'
    BrandDF = BrandDF.drop_duplicates()
    BrandDF.to_csv(dirs,encoding='gb18030',index=False,columns=[u'所属分类',u'店面招牌',u'优惠措施',u'店面地址',u'评价等级',u'评价数量',u'平均消费'])
    