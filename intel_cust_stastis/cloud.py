# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:30:26 2016

@author: changlue.she
"""

from wordcloud import WordCloud
from PIL import Image
import numpy as np
import pandas as pd
mask=0
dirc = 'C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\project\MSXF\intel_cust\\statistics\\history\\'
QAdf = pd.read_csv(dirc+'keyTopic.csv',encoding='gbk')
 
 
picdir = 'C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\MSXF\\intel_cust\\statistics\\pics\\'
text = ''
for i,cate in enumerate(QAdf[u'所属分类']):
    text += (' '+cate.split('/')[-1])*QAdf[u'命中次数'][i]
text = text.split(' ')
text = ' '.join(text)
if mask:
    alice_mask = np.array(Image.open(picdir+'msxf3.jpg'))
    wordcloud = WordCloud(font_path='C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/intel_cust/pycode/simhei.ttf', 
                              background_color="white", mask=alice_mask).generate(text)
else:
    wordcloud = WordCloud(font_path='C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/intel_cust/pycode/simhei.ttf', 
                              background_color="white").generate(text)
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
fig = plt.gcf()
fig.set_size_inches(10, 10)
plt.imshow(wordcloud)
plt.axis("off")