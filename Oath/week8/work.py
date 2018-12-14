# 16、实现一个函数判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出现的地址；否则返回None
str1 = 'qwer'
str2 = 'afsfqwerfdgfg'
def sub(fstr: str, tstr: str):
    '''
    :param fstr:
    :param tstr:
    '''
    if tstr.find(fstr) == -1:
        return None
    return tstr.find(fstr)
print(sub(str1, str2))
#
def sub(fstr: str, tstr: str):
    '''
    :param fstr: str
    :param tstr: str
    '''
    start = 0
    length = len(fstr)
    for i, _ in enumerate(tstr):
        s = tstr[start:start + length]
        if len(s) < length:
            return None
        else:
            if fstr == s:
                return i
        start = i + 1
print(sub(str1, str2))
#
import re
def sub(fstr:str, tstr:str):
    '''
    :param fstr: str
    :param tstr: str
    '''
    regex = re.compile(fstr)
    try:
        index = regex.search(tstr).span()
        return index[0]
    except Exception:
        return None
print(sub(str1, str2))
#
# 17、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值
def find_sum(array: list, n: int):
    '''
    find two Arguments that the sum eq n.
    :param array: list
    :param n: int
    :return: list
    '''
    length = len(array)
    target = []
    for i in range(length):
        for j in range(i + 1, length):
            if array[i] + array[j] == n:
                target.append((array[i], array[j]))
    return target


lst = [1, 3, 5, 7, 9, 7]
n = 10
print(find_sum(lst, n))