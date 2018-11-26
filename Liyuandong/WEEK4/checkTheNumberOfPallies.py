#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 法一
s = str('abcba')

if s[0] == s[4] and s[1] == s[3]:
    print('the "%s" is number of pallies' % s)
else:
    print('the "%s" is not number of pallies' % s)

# 法二

s = str(12321)

if s == s[::-1]:
    print('the "%s" is number of pallies' % s)
else:
    print('the "%s" is not number of pallies' % s)



# 法三
s = str('abcdedcba')
flag = True
for i in range(len(s) // 2):
    if s[i] != s[-i -1]:
        flag = False
        break
if flag:
    print('the "%s" is number of pallies' % s)
else:
    print('the "%s" is not number of pallies' % s)

"""
(0 + 0)

    方法一不够通用，代码用函数封装起来！
"""