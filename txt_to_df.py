#!/usr/bin/python
# coding: utf-8 -*-

#https://github.com/amitkaps/text-mining/tree/master/notebook/data-tau

import pandas as pd
import sys
import codecs

datafile = codecs.open('dataTau.txt',"rb", encoding='utf-8')

df = pd.DataFrame(columns=['Lines'])

for lines in datafile:
    df.loc[df.shape[0]] = lines.strip('\n\r')    

df.to_excel('op.xls',index=None)