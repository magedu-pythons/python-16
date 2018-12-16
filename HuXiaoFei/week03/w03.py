#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__='Storm'

"""
第三周作业：10.22-10.28
1、给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
2、任一个英文的纯文本文件，统计其中的单词出现的个数。
"""


# 1、给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
"""
思路：
1，确保给出的是一个列表
2，确保x元素是否是列表中的元素
3，有返回值，可print，可return
"""
#
# def foo(list_int, x):
#     if isinstance(list_int, list):
#         if x in list_int:
#             print(1)
#         else:
#             print(0)
#     else:
#         print("输入的不是一个列表类型。")
#
# foo([1,2,3,5], 1)





# 2、任一个英文的纯文本文件，统计其中的单词出现的个数。

li = []
sum_num = 0
with open('1.txt', 'r', encoding='utf-8') as f:
    a = f.readlines()  # 读取所有行并返回列表,包括换行符。['hello world\n', 'how are you\n', 'fine Thank you']
    for i in a:
        i = i.strip('\n')    # 去除换行符
        res1 = i.split(" ")  # 按空格分割
        for j in res1:       # 遍历每个元素并加入到新的列表中
            li.append(j)

    for k in li:
        if k.isalnum():  # 判断是否包含特殊符号
            if k.isalpha():  # 判断是否不含数字
                sum_num += 1
    print("共有%s个单词。" % sum_num)  # 包含重复单词统计