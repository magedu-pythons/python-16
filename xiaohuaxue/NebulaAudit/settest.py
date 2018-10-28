
import random
b=[]
c=[]

for i in range(10):
    a=random.random()
    a *= 10
    a += 10
    b.append(int(a))
print('第一组数据{}'.format(b))
for i in range(10):
    a=random.random()
    a *= 10
    a += 10
    c.append(int(a))
print('第二组数据{}'.format(c))
d = set(b) | set(c)
print('两组一共有{}个不同的数字'.format(len(d)))
e = d - (set(b)&set(c))
print('两组不重复的数字{}'.format(e))
print('两组重复的数字{}'.format(set(b)&set(c)))