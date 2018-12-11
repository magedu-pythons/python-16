#!/usr/bin/env python
# coding:utf-8
'''
问题描述：一个五位数，判断它是不是回文数
'''
#回文数： 就是一个数正向看和反响看相等 eg :123321
#answer1
Number1=int(input("please input five interger"))
str1=str(Number1)
Number2=str1[::-1]  #reseverd 12321 >>12321
if Number2 == Number1 :
    print( "%d is a palindromic"  % Number1)
else :
    print ("%d is not a palindromic" %Number1)

#way2
def Palindromic(Number):
    str1 = str(Number)
    length=len(str1)
    for i in range(length//2):
        if str1[i] == str1[-i-1]:
            return'{}is a palindromic'.format(Number)
        else:
            return '{}is a not palindromic'.format(Number)
Palindromic(input("please input five interger")
        print ()
        

