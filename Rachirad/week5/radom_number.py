#!/usr/bin/env python
"""
1打乱一个排好序的list对象alist,alist=[1,2,3,4,5]
"""
#shuffle(x, random=None) method of Random instance
# Shuffle list x in place, and return None.
import random
alist=[1,2,3,4,5]

def random_list(alist:list):
    random.shuffle(alist)
    return alist

#answer2
"""
已知仓库里有若干商品，以及相应库存，类似：
袜子,10
鞋子,20
拖鞋,30
项链,40

要求随机返回一直商品，商品被返回的概率与其库存成正比，要求描述思路或者直接写一个实现的函数


"""
#思路就是要成线性关系，把这些写商品看成一个成正比的算式的list
def products(shopping_list):
    sockets=10*'socket' #定义线性关系的表达式
    shoes=20*'shoes'
    t_shoes=30*'t_shoes'
    necklace=40*'necklace'
    shopping_list=[sockets,shoes,t_shoes,necklace]
    return random.choice(shopping_list)


