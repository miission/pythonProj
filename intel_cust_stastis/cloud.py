# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:30:26 2016

@author: changlue.she
"""

from wordcloud import WordCloud
from PIL import Image
import numpy as np
 
from keyWord import ALL_term
mask=1
text = ' '.join(ALL_term)
if mask:
    alice_mask = np.array(Image.open('C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/MSXF/ZhiChi/Statistic/pics/msxf3.jpg'))
    wordcloud = WordCloud(font_path='C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/MSXF/ZhiChi/Statistic/pics/simhei.ttf', 
                              background_color="white", mask=alice_mask).generate(text)
else:
    wordcloud = WordCloud(font_path='C:/Users/Administrator.NBJXUEJUN-LI/Desktop/project/MSXF/ZhiChi/Statistic/pics/simhei.ttf', 
                              background_color="white").generate(text)
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
fig = plt.gcf()
fig.set_size_inches(10, 10)
plt.imshow(wordcloud)
plt.axis("off")