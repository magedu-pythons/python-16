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
    f.close()

d = {}
for key in L:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
print(d)