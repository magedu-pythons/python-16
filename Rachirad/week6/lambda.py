#!/usr/bin/env python
"""
1现有二祖元祖，（（'a'）('b')）,(('c')'('d')),请使用python中的匿名函数生成列表[{'a':'c'},{'b':'d'}]

"""
#lambda函数
def func1(*args):
    tup1= (('a'),('b'))
    tup2 = (('c'),('d'))
    func1 = lambda  x,y:[{x[0]:y[0]},{x[1]:y[1]}]
    return func1(tup1,tup2)
    

#way2

def func():
    tup1=(('a'),('b'))
    tup2=(('c'),('d'))
    func=lambda tup1,tup2 :[{i:j} for i,j in zip(tup1,tup2)]
    return(func(tup1,tup2))


"""
输入一个英文句子，翻转句子中单词顺序，但单词内字符顺序不变
"""
astring="I like bing jing,i will visis Pk next year,so i  must wokr hard,learn more skills,just fly!!!! "

#reversed()函数
遗留
