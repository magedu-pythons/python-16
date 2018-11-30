#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__='Storm'


"""
第四周作业：11.5-11.11
1、问题描述：一个5位数，判断它是不是回文数。
2、随机生成20个数字，并且筛选出其中最大的3个数
"""


# 1、问题描述：一个5位数，判断它是不是回文数。
"""
回文数，即是给定一个数，这个数顺读和逆读都是一样的。例如：12321，13231是回文数，12345，123123不是回文数

思路：
5位的回文数规律，个位与万位相同，十位与千位相同，假设a=12321, a//10000 == a%10

"""
# num = input("请输入一个五位数：").strip()
#
# if num.isdecimal():
#     if len(num) == 5:
#         num = int(num)
#         if [num // 10000] == [num % 10]:
#             print('是回文数')
#         else:
#             print('不是回文数')
#     else:
#         print('请输入一个五位数。')



# 2、随机生成20个数字，并且筛选出其中最大的3个数
"""
首先确保都是数字
其次没有要求这个数字是几位，所以这里假定最大2位数
生成20个数字，没有说明是否允许出现重复，这里假定没有重复的数字
比较20个数字大小，从大到小打印前三个数
"""
import random

def random_num(n):
    """
    生成一个n范围内的随机数
    :param n:
    :return:
    """
    num = random.sample(range(0, n), 20)  # 随机生成不相同的数字，最小为0，最大为n
    return num


def max_num(n):
    """
    比较n范围内20个随机中最大的三个数
    :param n:
    :return:
    """

    nums = sorted([i for i in random_num(n)], reverse=True)

    return  nums[0],nums[1],nums[2]


print(max_num(100))

