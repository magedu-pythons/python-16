#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__='Storm'


"""
1、打乱一个排好序的list对象alist，alist=[1,2,3,4,5]:
"""
# import random
#
# alist = [1,2,3,4,5]
#
# random.shuffle(alist)
#
# print(alist)





"""
2、已知仓库中有若干商品，以及相应库存，类似：
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数 
"""

import random

# 假设扩大100倍库存数量
Wa_Zhi = ['WZ'] * 100
Xie_Zi = ['XZ'] * 200
Tuo_Xie = ['TX'] * 300
Xiang_Lian = ['XL'] * 400

# 将所有商品所有数量放在一个列表中
All_Before = Wa_Zhi + Xie_Zi + Tuo_Xie + Xiang_Lian

All_After = random.sample(All_Before, 100)  # 随机在列表中取100个元素

# 统计此100个元素中个商品出现的个数。
print(All_After.count('WZ'))
print(All_After.count('XZ'))
print(All_After.count('TX'))
print(All_After.count('XL'))

# 此题没思路，网络中找的答案。





