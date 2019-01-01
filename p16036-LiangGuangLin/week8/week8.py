'''
本周作业来袭，各位宝宝继续加油啊（12.10-12.16）
1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出现的地址；否则，返回None。
2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
'''

#----第一题----
def String_match(str1,str2):
    '''
	实现一个函数用于判断字符串str2是否是str1的子串
    str1: 长字符串1
    str2: 待匹配的字符串2
    :return: 字符串2在字符串1中首次出现的地址
    '''
    for i in range(len(str1)):
        if str1[i] == str2[0]:
            ind = i if str1[i:len(str2)+1] ==str2 else None
            return ind
    else:
        return ind

str1 = 'abcdef'
str2 = 'bcd'
print(String_match(str1,str2))

#----第二题----
def values_nums(lst,d_sum):
    '''
	给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值
    :param lst: 整数列表
    :param d_sum: 指定的值
    :return: 2个数的元组
    '''
    lst1 = [(i,d_sum-i)  for i in lst if ((d_sum-i) in lst) ]
    return lst1

lst =[1,5,2,7,4,9]
d_sum = 11
print(values_nums(lst,d_sum))