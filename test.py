import pandas as pd
import numpy as np
import scipy as sp
import random
from pandas import Series,DataFrame
random.seed(1)

doc121 = pd.read_csv('fmli121x.csv')
doc122 = pd.read_csv('fmli122.csv')
doc123 = pd.read_csv('fmli123.csv')
doc124 = pd.read_csv('fmli124.csv')
doc131 = pd.read_csv('fmli131.csv')

varname1 = ['NEWID','CUID']
contkeep=['AS_COMP1', 'AS_COMP2', 'AS_COMP3','AS_COMP4', 
          'AS_COMP5', 'PERSLT18','PERSOT64','NO_EARNR','PRINEARN']
catkeep=['AGE_REF','REF_RACE','HIGH_EDU','BLS_URBN', 'CUTENURE', 'EARNCOMP','INCLASS']
varn6_5 = ['FOODPQ','ALCBEVPQ','HOUSPQ', 'APPARPQ','TRANSPQ','HEALTHPQ','ENTERTPQ','PERSCAPQ', 'READPQ','EDUCAPQ','TOBACCPQ','MISCPQ','CASHCOPQ','PERINSPQ','TOTEXPPQ']
varname = np.hstack((varname1,contkeep,catkeep,varn6_5))

dat122 = doc122.loc[:,varname]
dat123 = doc123.loc[:,varname]
dat124 = doc124.loc[:,varname]
dat131 = doc131.loc[:,varname]

data = pd.concat([dat122,dat123,dat124,dat131])

def test_1():
    assert set(data.columns.values)==set(varname)
    




    
    