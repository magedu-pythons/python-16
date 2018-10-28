#!/usr/bin/env python
#condig:utf-8

#the test of  Thrid week 


"""任意一个纯文本文件，统计其中单词出现个数
"""
import re
r=re.compile(r'\b[a-zA-Z]+(\'[msdt])?\b')
file=open('2.txt','r')
s=file.read()
m=r.findall(s)
L=len(m)
print(L)
