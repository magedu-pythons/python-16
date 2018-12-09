#!/usr/bin/env python
#coding=utf-8
def is_palindromic(num: int):
    s1 = str(num)
    s2 = s1[::-1]
    # reversed  abc->cba  aba -> aba
    if s1 == s2:
        print( '{} is palindromic'.format(num))
    else:
        print( '{} is not palindromic'.format(num))
is_palindromic(input("please input interger:"))
