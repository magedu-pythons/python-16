# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 17:09
# @Author  : huo la la
# @Email   : xblinux06@gmail.com


"""
    I am a Student,I love Python,ha ha ha

    the program include python's modules import, time,datetime,how to use print and simple functions
"""

import time
import datetime

def print_me_info():

    print("I say:\"Hello,My Friend! {date}\"").format(date=datetime.datetime.now())
    time.sleep(1)
    print("I say:\"My name is Roddy {date}\"").format(date=datetime.datetime.now())
    time.sleep(2)
    print("I say:\"I'm 25 years old {date}\"").format(date=datetime.datetime.now())
    time.sleep(2)
    print("I say:\"I am pythoner {date}\"").format(date=datetime.datetime.now())
    time.sleep(1)
    print("I say:\"Bye {date}\"").format(date=datetime.datetime.now())

print_me_info()
