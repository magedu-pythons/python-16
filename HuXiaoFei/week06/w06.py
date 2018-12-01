#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__='Storm'



'''
1、现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
'''

"""
print(list(zip(t1,t2))) #  [('a', 'c'), ('b', 'd')]
for i in list(zip(t1,t2)):
    print(i)  # ('a', 'c')  ('b', 'd')

a = []
for i,j in list(zip(t1,t2)):
    print([{i: j}])  # [{'a': 'c'}]  [{'b': 'd'}]
    a.append({i: j})
print(a)

"""

# t1 = (('a'),('b'))
# t2 = (('c'),('d'))
# func = lambda x, y: [{i:j} for i, j in zip(x, y)]
# print(func(t1, t2))







'''
2、输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变 
'''

word = "Success is the sum of small efforts, repeated day in and day out."

a  = word.split(" ")
# print(a)  # ['Success', 'is', 'the', 'sum', 'of', 'small', 'efforts,', 'repeated', 'day', 'in', 'and', 'day', 'out.']

# print(a[::-1])  # ['out.', 'day', 'and', 'in', 'day', 'repeated', 'efforts,', 'small', 'of', 'sum', 'the', 'is', 'Success']

print(" ".join(a[::-1]))  # out. day and in day repeated efforts, small of sum the is Success

c = []
for i in a:
    for j in i:
        if "." in j:
            print(i)  # efforts,
        elif "," in j:
            print(i)  # out.
# 问题：如何移位？将,和.移到前面？