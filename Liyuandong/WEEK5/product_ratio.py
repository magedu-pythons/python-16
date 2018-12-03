#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def productRatio(n):
    target = random.randint(0, sum(n.values()))    # 获取随机数
    s = 0
    for k,v in n.items():
        s += v
        if s >= target:      #判断区间
            return k



if __name__=='__main__':
    d = {
        'socks': 10,
        'shoes': 20,
        'slipperrs': 30,
        'necklace': 40
    }
    print(productRatio(d))