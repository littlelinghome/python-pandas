#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午2:34
# @Author  : littlelinghome
# @Site    : 
# @File    : 1.py
# @Software: PyCharm

import numpy as np

"""
一维数组
"""
#numpy 模块创建数据
data = np.array([1,2,3,4])  #参数是列表
print(data)

#查看数组data的属性:几维数组
print(data.shape)  #一维数组，共4个元素

#查看数组data的属性:元素数据类型
print(data.dtype)

#利用索引查看数组元素
print(data[1])

#修改数组元素
data[1] = 9
print(data)


"""
二维数组
"""
# numpy 模块创建二维数组
data = np.array([[1,2,3],[4,5,6]]) #参数仍然是一个列表，大的列表里面嵌套了2个小的列表
print(data)

# 查看数组data的属性:几维数组
print(data.shape)

# 利用索引查看数组元素
print(data[1,2])

#修改数组元素
data[1,2] = 0
print(data)


"""
另外一种创建二维数组的方法
"""
data = np.arange(10)
print(data)

data = np.arange(5,15)
print(data)


"""
把一维数组转变为二维数组
reshape 并没有copy数组，而是返回数组的一个视图
不是拷贝，而是引用
"""
data = np.arange(10)
data1 = data.reshape(2,5)
print(data1)

# 原数组data改变，那么data1也会发生改变
data[4] = 0
print(data)
print(data1)


"""
利用numpy生成一些特殊的数组
"""
#生成全是0的二维数组
data = np.zeros((2,2))
print(data)

#生成全是1的3维数组
data = np.ones((2,3,3))
print(data)

#生成一个4行4列的对角数组
data = np.eye(4)
print(data)


"""
利用reshape，把一维数组reshape成我们想要的多维数组
"""
data = np.arange(16).reshape(4,4)
print(data)