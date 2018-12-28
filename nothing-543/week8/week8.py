str1 = input('>>>string1')
str2 = input('>>>string2')

def find_index(str1:str, str2:str):
    """
    实现一个函数用于判断字符串str2是否是str1的子串。
    如果是，则该函数返回str2在str1中首次出 现的地址；
    否则，返回None。
    """
    index = str1.find(str2)
    if index < 0:
       index = None
    return index


lst = [1,5,2,7,4,9]
sum = int(input('>>>'))

def find_sum(lst:list, sum:int):
    """
    给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？

    """
    for i, val in enumerate(lst):
        poor = sum - lst[i]
        for j in range(i + 1, len(lst)):
            if lst[j] == poor:
                return lst[i], lst[j]


"""
(0 + 0)

    建议第二题参考答案，另在实现一次
"""