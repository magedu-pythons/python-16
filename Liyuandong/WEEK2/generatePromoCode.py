#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 使用random模块进行生成优惠券
import random
for i in range(200):
    L = []
    big_str = chr(random.randint(97, 122))
    little_str = chr(random.randint(65, 90))
    num = str(random.randint(0, 1000))
    for i in range(6):
        promo_code = random.choice((big_str, little_str, num))
        L.append(promo_code)
    print(''.join(L))

# 使用hashlib
import hashlib, random
for i in range(200):
    L = []
    for i in range(6):
        m = hashlib.md5(b'chr[random.randint(0, 126)]').hexdigest()
        promo_code = random.choice(m)
        L.append(promo_code)
    print(''.join(L))