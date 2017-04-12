# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:07:44 2016

@author: changlue.she
"""
from __future__ import division
import datetime
from sklearn.datasets import make_hastie_10_2
 
from sklearn.metrics import roc_auc_score
X, y = make_hastie_10_2(random_state=0)
##################
import pandas as pd
#import numpy as np
import lightgbm as lgb
X_train, X_test =X[:10000], X[10000:]
y_train, y_test =y[:10000],y[10000:]
 
 
#X_train = np.repeat(X_train,10, axis=0)
#y_train = np.repeat(y_train,10)
#df = pd.DataFrame(X_train)
#df['label'] = y_train
#df.to_csv('C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\tmpProj\\rootGBM\\rootGBM\\train.csv',encoding='gbk',index=0)
#df = pd.DataFrame(X_test)
##########################################################
print ('light gbm')
for i in range(1,11):
    params = {
        'boosting_type': 'gbdt',
        'objective': 'binary',
        'metric': 'binary_logloss',
        'num_threads':2,
       'learning_rate':0.1*i,
       'num_leaves':2,
     
       'feature_fraction': 0.1,
        'bagging_fraction': 1,
    }
    lgb_train = lgb.Dataset(X_train, y_train)
    a = datetime.datetime.now()
    gbm = lgb.train(params,lgb_train,num_boost_round=10000)
    b = datetime.datetime.now() 
    print (b-a)
    y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
    print (i,roc_auc_score(y_test,y_pred))
  
##########################################################
print ('rootGBM')
import  rootGBM  
trainset = rootGBM.Dataset(X_train, y_train,100,1)
for i in range(1,11):
   
    a = datetime.datetime.now()
    rgbm = rootGBM.rootGBMClassifier(trainset,0.1*i,10000,2,1)
    b = datetime.datetime.now() 
    print (b-a)
    y_pred = rgbm.predict(X_test)
    print (i,roc_auc_score(y_test,y_pred))
##########################################################  
rawdata = pd.read_csv('C:\\Users\\Administrator.NBJXUEJUN-LI\\Desktop\\project\\tmpProj\\rootGBM\\rootGBM/out.csv',
                      header=0,encoding='gbk' )
y_pred = rawdata['score']
print (roc_auc_score(y_test,y_pred))
