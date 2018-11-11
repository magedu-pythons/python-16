# 打印出100以内的斐波那契数列,方法一
a = 0
b = 1
while b < 100:
    print(b)
    a, b = b, a+b


# 打印出100以内的斐波那契数列,方法二
lst = [1, 1]
i = 0
while lst[i] + lst[i+1] < 100:
    lst.append(lst[i] + lst[i+1])
    i += 1
print(lst)


"""
(0 + 0)
    
    方法2 本质跟1是一样的，考虑其他方式
"""