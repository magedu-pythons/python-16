# -*- coding: utf-8 -*-
"""
******************************************************************
日期：2018-10-19
作者: LiangGuangLin
描述：斐波那契数列、随机优惠码
******************************************************************
"""

################第2题：生成斐波那契数列#######################
#===方法1=====
lst_f =[1,1]             
for i in range(2,100):
    a = lst_f[i-1]+lst_f[i-2]
    if a> 100:
        break
    lst_f.append(a)
print(lst_f)

#===方法2=====
num0 = 1
num1 = 1
for i in range(2,100):
    num0,num1 = num1,(num0+num1)     #*右移
    print(num0)
    if num1> 100:
        break

################第2题：生成随机优惠#######################
import random
from random import choice

foo = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k',1,2,3,4,5,6,7,8,9,0]
dic_code = {}
for i in range(300):
    n = random.randint(6,9)
    lst = random.sample(foo,n)
    str1 = ''.join(map(str,lst))   #* p(s
    dic[str1] = i
    if len(dic) >= 200:
        break
print('非重复优惠码：',dic)

"""
(0 + 0)

    2、dic变量不存在，写完代码记得测试成功后提交
"""