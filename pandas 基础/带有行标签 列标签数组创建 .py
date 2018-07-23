#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午10:29
# @Author  : littlelinghome
# @Site    : 
# @File    : 1.py
# @Software: PyCharm

"""
官方快速入门pandas文档
http://pandas.pydata.org/pandas-docs/stable/10min.html
"""

import pandas as pd
import numpy as np


"""
创建pandas里面的关键数据结构，Series 创建一维数据
"""
# Series 代表一行或者一列的一维数组，并自动带有索引
s = pd.Series([1,3,5,np.NaN,8,4])  #参数是列表
print(s)


"""
DataFrame 创建二维数组
"""
dates = pd.date_range('20160301',periods=6)
print(dates)
data = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(data)

#查看data是几维数组
print(data.shape)

#查看data的元素值
print(data.values)


"""
利用字典创建二维数组
"""
d = {'A':1,'B':pd.Timestamp('20130301'),'C':range(4),'D':np.arange(4)}
print(d)

df = pd.DataFrame(d)
print(df)

# 查看df各个列的属性
print(df.dtypes)

# 访问 A列
print(df.A)

# 访问B列
print(df.B)

# 查看B的属性
print(type(df.B))

