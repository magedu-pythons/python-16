#!usr/bin/python
# -*- coding:utf-8 -*-
# @Time     :2018/11/11 18:01
# @Author   :Sai Zhou
# @Filename :week2.py
# @Software :PyCharm
# @Function :------

###### 打印出100以内的斐波那契数列，使用2种方法实现 ######
    ### method 1 ###
a = 0
b= 1
while b<100:
    print(b)
    a,b = b,a+b

    ### method 2 ###
a,b = 0,1
list = []
while a <100:
    print(a,end=' ')
    list.append(a)
    a,b = b,a+b
###### 使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上 ######
import random
total = 'abcdefghijklmnopquABCDEFGHIJKLMNOPQRSTUVW123456789@#$%&*'
for i in range(200):
    codes = []
    for j in range(6):
        code=''.join(random.sample(str.upper(total),5))
        codes.append(code)
    print('-'.join(codes))