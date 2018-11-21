# 打乱一个排好序的list对象alist，alist=[1,2,3,4,5]
import random

# 方法一：就地打乱
def scatter1(src):
    for i in range(len(src)):
        j = random.randint(0, i)
        src[i], src[j] = src[j], src[i]

    return src


# 方法二：返回新列表
def scatter2(src):

    return [src[i] for i in random.sample(set(range(len(src))), len(src))]


alist = [1, 2, 3, 4, 5]
print(scatter1(alist))
print(scatter2(alist))