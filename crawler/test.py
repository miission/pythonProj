# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 15:47:34 2017

@author: changlue.she
"""

#encoding=utf-8
import urllib2
import cookielib
from bs4 import BeautifulSoup
#登陆页面，可以通过抓包工具分析获得，如fiddler，wireshark
url = "https://list.tmall.com/search_product.htm?spm=875.7931836/A.subpannel2016025.1.Hshj73&oq=%C5%AE%D7%B0&active=1&acm=2016031463.1003.2.1398732&sort=new&industryCatId=50025135&pos=1&cat=50025135&prop=122216347:740138901&style=g&from=sn_1_prop&search_condition=4&scm=1003.2.2016031463.OTHER_1482953610356_1398732#J_crumbs"
     
#获得一个cookieJar实例
cj = cookielib.CookieJar()
#cookieJar作为参数，获得一个opener的实例
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#伪装成一个正常的浏览器，避免有些web服务器拒绝访问。
#opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
#生成Post数据，含有登陆用户名密码。
 
#以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie
#opener.open(url)
#以带cookie的方式访问页面
op=opener.open(url)
#读取页面源码
 
soup=BeautifulSoup(op.read())
soup.findAll('link')
 