#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 法一
import random
alist = [1, 2, 3, 4, 5]
random.shuffle(alist)
print(alist)

# 法二
import random
alist = [1, 2, 3, 4, 5]
L = []
for i in range(len(alist)):
    s = random.choice(alist)
    L.append(s)
    alist.remove(s)
print(L)

# 法三
import random
def scrambList(s):
    for i in range(len(s)):
        j = random.randint(0, i)
        s[i], s[j] = s[j], s[i]
    return s
alist = [1, 2, 3, 4, 5]
print(scrambList(alist))

"""
(0 + 0)

    用函数封装代码
"""