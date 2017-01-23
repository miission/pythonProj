# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:15:54 2017

@author: changlue.she
"""

import urllib2
    
import urllib
  
from bs4 import BeautifulSoup
import pandas as pd
import re
'''get the first class categories'''
url = 'http://club.jd.com/review/2967927-3-1.html'
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent
req=urllib2.Request(url,headers=header)
response=BeautifulSoup(urllib2.urlopen(req,None))
response.find('div',{'class':'comment-item'})