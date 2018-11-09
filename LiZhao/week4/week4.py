################第五周作业

#判断一个数是否随机数
def pn():
    _pn = input('请你输入一个五位数的数字:')
    if _pn[0] == _pn[-1] and _pn[1] == _pn[-2]:
        print('这是一个回文数')
    else:
        print('这不是一个回文数')


pn()


#####################################
#随机生成20个随机数,求最大的三个
import random


def ma():
    seq = random.sample(range(100), 20)
    print(seq)
    num = sorted(seq)
    print(num[-1], num[-2], num[-3])


ma()
