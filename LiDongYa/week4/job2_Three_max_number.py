# 随机生成20个数字，并且筛选出其中最大的3个数 
import random

source = [random.randint(1, 100) for i in range(20)] # 源数据
print(source)                                        # 显示源数据

def maxnumber(lst, n, maxnums=None): # 参数lst为源数据，n为最大数的个数，maxnums最大数的容器
    if maxnums==None:
        maxnums = []
    s = set(lst)                     # 转换为set集合，去重，并在剔除最大值元素时，提高效率
    for i in range(n):
        maxnums.append(max(s))       # 添加最大值
        s.discard(max(s))            # 集合中去除最大值，方便下次查找
    return maxnums

maxnumber(source, 3)