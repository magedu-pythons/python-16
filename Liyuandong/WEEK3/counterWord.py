#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 法1
from collections import Counter

f = open('python.txt', 'r')
L = []
for i in f.readlines():
    L.append(i.strip('\n'))
f.close()
cnt = Counter()
for word in L:
    cnt[word] += 1
print(cnt)


# 法2
from collections import Counter

L = []
with open('python.txt', 'r') as f:
    for i in f.readlines():
        L.append(i.strip('\n'))
    f.close()
cnt = Counter()
for word in L:
    cnt[word] += 1
print(cnt)

# 法3

L = []
with open('python.txt', 'r') as f:
    for i in f.readlines():
        L.append(i.strip('\n'))

d = {}
for key in L:
    if key not in d:
        d[key] = 1
    else:
        d[key] += 1
print(d)


"""
(0 + 0)

    做的不错,需要考虑去点一些标点符合非单词
"""