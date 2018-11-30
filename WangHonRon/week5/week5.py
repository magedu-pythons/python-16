"""
1、打乱一个排好序的list对象alist，alist=[1,2,3,4,5]
2、已知仓库中有若干商品，以及相应库存，类似：
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数
"""
#one upset seq
import random
alist = [1,2,3,4,5]
def upset(alist):
    for i in range(len(alist)):
        intnum = random.randint(0,len(alist)-1)
        random.shuffle()
        print(intnum)
        print(alist[i],alist[intnum])
        alist[i] ,alist[intnum] = alist[intnum], alist[i]
        print(alist[i],alist[intnum])
    return alist
print(upset(alist))

#two

