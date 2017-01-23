# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:21:07 2016

@author: changlue.she
"""
 
import urllib2
from bs4 import BeautifulSoup
import cPickle
import pandas as pd
'''get the first class categories'''
url = 'https://www.dianping.com/search/category/2/10/g110r1465'
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent
req=urllib2.Request(url,headers=header)
response=BeautifulSoup(urllib2.urlopen(req,None))
'''get all the stuffs that sale'''
allTypes = response.find('ul').findAll('li')
'''get food category of sales'''
for firstClassIdx in [0,1,2,3,4,8,9,11,12,13,14,15,16]:
    allFoodList = [] 
    foodTypes = allTypes[firstClassIdx].findAll('a')
    idx = 0
    firstClassName = foodTypes[0].text
    '''get subCategories's title'''
    crawledURL = []
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
                foodContents = foodResponse.find('div',{'class':'shop-list J_shop-list shop-all-list'}).findAll('li')
            except:
                next
            for foodContent in foodContents:  
                idx+=1 
                if idx%1000==0:
                    print firstClassName
                foddDetail = foodContent.find('div',{'class':'txt'})
                '''get titles'''
                try:
                    titles = foddDetail.find('div',{'class':'tit'}).findAll('a')
                    brand = titles[0].text.replace('\n','')
                    topTitle = '|'.join([tt.text for tt in titles[1:]])
                    if u'广告'in topTitle:
                        ifAD = "广告"
                    else:
                        ifAD = "没有广告"                 
                except:
                    next
                try:
                    promoSlogns = foddDetail.find('div',{'class':'tit'}).find('div',{'class':'promo-icon'}).findAll('a')
                    promoSlogn = '###'.join([promoSlogn['title'] for promoSlogn in promoSlogns])
                except:
                    promoSlogn = 'no promoSlogn'
                '''get comments'''
                comments = foddDetail.find('div',{'class':'comment'}) 
                try:
                    stars = comments.find('span')['title']
                except:
                    stars = -1
                try:
                    reviewNums = comments.find('a',{'class':'review-num'}).find('b').text
                except:
                    reviewNums = -1
                try:
                    meanPrice  = comments.find('a',{'class':'mean-price'}).find('b').text.replace(u'￥','')
                except:
                    meanPrice = -1
                '''get address'''
                try:
                    address =  foddDetail.find('div',{'class':'tag-addr'}).find('span',{'class':'addr'}).text
                except:
                    address = -1            
                '''get rate detail'''  
                try:
                    rates = foddDetail.find('span',{'class':'comment-list'}).findAll('span')
                    rates = [rate.find('b').text for rate in rates]
                    if len(rates)<3:
                        rates = [-1,-1,-1]
                except:
                    rates = [-1,-1,-1]
                allFoodList.append([subFoodTypeName,brand,ifAD,promoSlogn,stars,reviewNums,meanPrice,address]+rates)
                 
    #------------------------------------------------------------------------------
    '''pick save and load the brands'''
    dirs = "C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\Python\\NLP\\savedObject\\meituan\\"
    dirs = dirs+firstClassName+'.pkl'
    cPickle.dump(allFoodList,open(dirs,"wb")) 
    allClassLoads = cPickle.load(open(dirs,"rb"))
    #------------------------------------------------------------------------------
    '''save the brands into csv'''
    BrandDF = pd.DataFrame(allFoodList,columns=[u'所属分类',u'店面招牌',u'是否广告',u'优惠措施',u'评级等级',u'评价数量',u'平均消费',u'店面地址',u'未知字段1',u'未知字段2',u'未知字段3'])
    dirs = 'C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\MSXF\\feature construct\\doc\\meituan\\'
    dirs = dirs+firstClassName+'.csv'
    BrandDF = BrandDF.drop_duplicates()
    BrandDF.to_csv(dirs,encoding='gb18030',index=False,columns=[u'所属分类',u'店面招牌',u'是否广告',u'优惠措施',u'评级等级',u'评价数量',u'平均消费',u'店面地址',u'未知字段1',u'未知字段2',u'未知字段3'])
     