'''
第九周作业班主任-薇薇 12月17号 星期一 13:58
各位小伙伴又到了写作业的时候了哦，小伙伴们加油了哦~~
本周作业小伙伴看这里：
1、请实现函数 new_counter ，使得调用结果如下：
      c1 = new_counter(10)
      c2 = new_counter(20)
      print（c1(), c2(), c1(), c2()）
      outputs ：
      11 21 12 22
2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符
'''
#########################################################################
#-----第一题-------
def new_counter(i):
    a = [i-1]
    def add():
        a[0] = a[0] + 1
        return a[0]
    return add
c1 = new_counter(10)
c2 = new_counter(20)
print(c1())
print(c2())
print(c1())
print(c2())

#-----第二题--------
def str_rep(str1):
    '''
    判断字符串是否不含有重复字符
    :param str1: 字符串
    :return: 布尔值,若含有重复字符则返回True
    '''
    lst = [ s for s in str1]
    dic = set(lst)
    if len(dic) < len(lst):
        return True
    else:
        return False

str1 = 'aabbccc'
print(str_rep(str1))