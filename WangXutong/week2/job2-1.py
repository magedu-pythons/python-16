#coding=utf-8
import random
lst1 = []
#生产9个数字
for i in range(0,10):
    lst1.append(i)
    continue
#生成26个大写的字母
for j in range(65,91):
#把数字转换为ASCII码
    k=chr(j)
    lst1.append(k)
    continue
for u in range(97,122):
#把数字转换为ASCII码
    h=chr(u)
    lst1.append(h)
    continue
for i in range(200):
#生成10个元素组成的列表，并打印
    print(str(random.sample(lst1,20)))


 """
(0 + 0)

   修改成.py后缀文件
"""