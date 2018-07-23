#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午11:00
# @Author  : littlelinghome
# @Site    : 
# @File    : 2.py
# @Software: PyCharm

import pandas as pd
import numpy as np

dates = pd.date_range('20160301',periods=6)
data = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(data)
"""
表的各种查看方法
"""
#默认查看data数组的前5行数据
print(data.head())

#查看data数组的前2行数据
print(data.head(2))

#查看data数组的尾部数据，默认也是最后5行数据
print(data.tail())

#当然你也可以查看最后3行数据
print(data.tail(3))

#查看data的行标签
print(data.index)

#查看data的列标签
print(data.columns)

#查看data数组值
print(data.values)

#查看data数组元素数值的整体情况
print(data.describe())

#数组转置
print(data.T)


"""
表的排序
"""
#根据列标签进行排序（默认升序）
print(data.sort_index(axis=1))

#根据列标签倒叙排列
print(data.sort_index(axis=1,ascending=False))

#根据行标签进行排序,并且是倒叙排序
print(data.sort_index(axis=0,ascending=False))

#根据数组元素排序，根据某一列进行排序
print(data.sort_values(by='A'))



"""
二维表的选择
"""
# 选择某一列
print(data['A'])

#当然还有另外一种方法，属性值
print(data.A)

#选择3-4行
print(data[2:4])

#当然也可以通过行标签选择出想要的数据
print(data['20160302':'20160305'])

#还有一种效率较高的方式：loc函数  它效率高的原因是不再需要判断参数是位置参数还是内部元素参数，它只认标签
print(data.loc['20160302':'20160305'])

#利用位置抱歉选择数据
print(data.iloc[2:4])

# 只选择出 B，C两列数据
print(data.loc[:,['B','C']])

# 既选择列，也选择行
print(data.loc['20160302':'20160305',['B','C']])

#利用loc函数访问某个特定的值
print(data.loc['20160302','B'])

#另外一种更高效的访问某个元素的方法,但是它传入的参数必须是原生的数据结构，而不能直接是日期等
print(data.at[pd.Timestamp('20160302'),'B'])


#选择第二行
print(data.iloc[1])

#选择第2-3行
print(data.iloc[1:3])

#选择某行某列
print(data.iloc[1:3,2:4])

#选择某几列，所有的行
print(data.iloc[:,1:3])

#访问某个特定的元素
print(data.iloc[1,1])

#访问某个特定元素更高效的方法
print(data.iat[1,1])


"""
利用布尔索引选取数据
"""

#选取A列打印0的数据
print(data[data.A>0])

#选取data中所有大于0的数据,小于0的表示为 NaN
print(data[data>0])

#另外一种布尔索引的方式是：isin
data2 = data.copy()
tag = ['a']*2 + ['b']*2 + ['c']*2
data2['TAG'] = tag
print(data2)

print(data2[data2.TAG.isin(['a','c'])])


"""
修改二维表的元素
"""
#直接修改某个元素
data.iat[0,0] = 100

#直接修改某一行或者某一列
data.A = range(6)
print(data)

#直接利用标量来修改某一列
data.B = 200
print(data)