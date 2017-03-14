# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 22:18:35 2016

@author: zhangjc
"""
import pandas as pd

a = pd.Series([7,6,5,4,9])
print(a)

a = pd.Series([7,6,5],index=['shu','shuo','jun'])
print(a)

a= {'beijing':'7000','shanghai':'8000','shenzhen':'7700'}
print(a)
b = pd.Series(a)
print(b)


pop={'city':['chongqin','shanghai','beijing',
             'chengdu','tianjin','guangzhou',
             'baoding','harbin','suzhou','shenzhen'
             ],
      'pop':[2885,2301,1911,2211,4555,6666,7777,9999,
             34242,36
             ]
     }
print(pop)
pop_DF = pd.DataFrame(pop)
print(pop_DF)
pop_DF['country']='china'
print(pop_DF)
province = pd.Series(['guangdong','jiangsu'],index=[5,8])
pop_DF['province']=province
print(pop_DF)

#pd.to_csv('d:\\a.csv')
pop_DF.to_csv('d:\\b.csv')


gdp = pd.DataFrame([[11.61,13.08,13.67,15.05],[12.81,14.3,15.7,16.6],[13.87,15.5,16.35,17.87],[14.8,16.6,17.36,18.94]],
                index=['2012','2013','2014','2015'],columns=['s1','s2','s3','s4'])
print(gdp)
print(gdp.sum(axis=1))
print(pd.read_csv('d:\\b.csv'))


