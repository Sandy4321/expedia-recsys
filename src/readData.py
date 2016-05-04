# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import pandas as pd
import StringIO as StringIO
import matplotlib.pyplot as plt

kpath = '../data/'
dfile = 'destinations.csv'
trainfile = 'train.csv'
subfile = 'sample_submission.csv'
testfile = 'test.csv'

st_time = time.time()
destinations = pd.read_csv(kpath+dfile)
traindata = pd.read_csv(kpath+trainfile)
submission = pd.read_csv(kpath+subfile)
print('elapsed time:'+str(time.time()-st_time))