#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 法一
import random
L = []
for num in range(20):
    s = random.randint(1,1000)
    L.append(s)
print(sorted(L, reverse=True)[0:3])

# 法二
import random
L = []
S = []
for num in range(20):
    s = random.randint(1,1000)
    L.append(s)

for num in range(3):
    m = max(L)
    S.append(m)
    L.remove(m)
print(S)


