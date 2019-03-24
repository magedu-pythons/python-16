"""
第八周作业班主任-薇薇 今天 星期一 14:26
本周作业来袭，各位宝宝继续加油啊（12.10-12.16）
1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。
2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
"""

#No.1
def is_substr(substr,src):
    if substr in src:
        index  = src.find(substr)
        return index if index != -1 else None
print(is_substr('abd','ergabdrtrhabd'))

#No.2
def is_equl_num(lst:list,num:int):
    lt = [(item,item2) for item in lst for item2 in lst if item+item2 ==num ]

    return lt

print(is_equl_num([1,5,2,7,4,9],11))



"""
(0 + 0)

    第二题答案中有更好的实现
"""