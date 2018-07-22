#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午4:15
# @Author  : littlelinghome
# @Site    : 
# @File    : 数组的索引.py
# @Software: PyCharm


import numpy as np

"""
一维数组索引访问
"""
data = np.arange(100,step=10)
print(data)

#访问第三个元素
print(data[2])

#访问多个元素
print(data[2:5])

#访问第一个到第三个元素
print(data[:3])

#访问第六个元素到最后一个元素
print(data[5:])

#从第六个元素开始全部赋值为-1
data[5:] = -1
print(data)


"""
二维数组访问
"""
data = np.arange(16).reshape(4,4)
print(data)

#访问第二行数据
print(data[1])

#访问第二行至第三行数据
print(data[1:3])

#选择第三列至第四列
print(data[:,2:4])

# 行：2-3；列：3-4
print(data[1:3,2:4])


"""
利用数组的直接索引
"""
data = np.arange(16).reshape(4,4)

#返回的是2个元素，第一个元素是行1列2，第二个元素是行3列3
print(data[[1,3],[2,3]])

#上面的写法等价于
print(data[1,2])
print(data[3,3])


"""
利用布尔数组作为索引
"""
data = np.arange(16).reshape(4,4)

#同样返回一个4*4的二维矩阵，只不过矩阵的元素都是布尔类型
print(data > 10)

# 利用以上生成的布尔矩阵作为索引来访问数组,布尔数组中所有为True的元素都被选择出来，所有为False的元素都被忽略掉
idx = data > 10
print(data[idx])

#将以上两步骤合成在一起的写法
print(data[data>10])

#选择data中所有的偶数元素
print(data[data % 2 ==0])


"""
二维数组的运算
"""
x = np.arange(1,5).reshape(2,2)
print(x)
y = np.arange(5,9).reshape(2,2)
print(y)

#二个数组相加，对应位置上的元素相加
print(x + y)

# 利用函数来实现二个数组相加
np.add(x,y)

# 二个数组相乘，对应位置上的元素相乘
print(x * y)

# 矩阵内积
print(x.dot(y))


# 二个数组相除，对应位置上的元素相除
print(x / y)


"""
数组的一些其他运算方法
"""
x = np.arange(1,5).reshape(2,2)
# 求 X 的平方根
print(np.sqrt(x))

# 求 x 的转置
print(x.T)


"""
linsapce 的用法
"""
x = np.linspace(1,10)
print(x)

# 1-10之间划分成100份
y = np.linspace(1,10,num=200)
print(y)