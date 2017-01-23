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
for firstClassIdx in [10]:
    allFoodList = [] 
    foodTypes = allTypes[firstClassIdx].findAll('a')
    idx = 0
    firstClassName = foodTypes[0].text
     
    '''get subCategories's title'''
    for foodType in foodTypes[1:]:
        subFoodTypeName = foodType.text
        subFoodTypeUrl  = foodType['href']
         
        while(subFoodTypeUrl!='None'):
            try:                
                foodReq=urllib2.Request(subFoodTypeUrl,headers=header)
                foodResponse=BeautifulSoup(urllib2.urlopen(foodReq,None))         
                subFoodTypeUrl = 'http://www.dianping.com'+ foodResponse.find('div',{'class':'page'}).find('a',{'class':'next'})['href']          
            except:
                subFoodTypeUrl = 'None'
            try:    
                foodContents = foodResponse.find('ul',{'class':'hotelshop-list'}).findAll('li')
            except:
                next
            for foodContent in foodContents:  
                idx+=1 
                if idx%1000==0:
                    print firstClassName
                try:
                    shopUrl = 'http://www.dianping.com'+ foodContent.find('a')['href']
                    shopReq=urllib2.Request(shopUrl,headers=header)
                    shopContent=BeautifulSoup(urllib2.urlopen(shopReq,None)) 
                except:
                    next
                
                try:
                    baseInfo = shopContent.find('div',{'class':'hotel-base-info'})
                
                    brand = baseInfo.find('h1').text.replace('\n','')
                except:
                    next
                try:                    
                    review = baseInfo.find('p',{'class':'info shop-star'}).findAll('span') 
                    rate =  p.findall(review[0]['class'][1])[0]                
                    reviewNum = p.findall(review[1].text)[0]
                except:
                    rate = -1
                    reviewNum = -1
                try:
                    address = baseInfo.find('p',{'class':'shop-address'})
                except:
                    address = -1
                try:
                    tags = shopContent.find('div',{'class':'outstanding-block user-tags'}).find('p',{'class':'J_shop-tags'}).findAll('a')
                    tags = '###'.join([tag.text.replace('\n','').replace(' ','') for tag in tags])
                except:
                    tags = -1
                allFoodList.append([subFoodTypeName,brand,rate,reviewNum,address,tags])
             
    #------------------------------------------------------------------------------
    '''pick save and load the brands'''
    dirs = "C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\Python\\NLP\\savedObject\\meituan\\"
    dirs = dirs+firstClassName+'.pkl'
    cPickle.dump(allFoodList,open(dirs,"wb")) 
    allClassLoads = cPickle.load(open(dirs,"rb"))
    #------------------------------------------------------------------------------
    '''save the brands into csv'''
    BrandDF = pd.DataFrame(allFoodList,columns=[u'所属分类',u'店面招牌',u'评价等级',u'评价数量',u'店面地址',u'用户标签'])
    dirs = 'C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\MSXF\\feature construct\\doc\\meituan\\'
    dirs = dirs+firstClassName+'.csv'
    BrandDF = BrandDF.drop_duplicates()
    BrandDF.to_csv(dirs,encoding='gb18030',index=False,columns=[u'所属分类',u'店面招牌',u'评价等级',u'评价数量',u'店面地址',u'用户标签'])
    