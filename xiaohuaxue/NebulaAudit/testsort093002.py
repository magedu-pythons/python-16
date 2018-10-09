import datetime
import random
a = []
for c in range(10000):
    rand = random.randint(0, 10000)
    a.append(rand)
start = datetime.datetime.now()
flag = False
length = len(a)-1
for i in range(len(a)):
    for j in range(length):
        if a[j] < a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            flag = True
    length -= 1
    if not flag:
        break
print(a)
end = datetime.datetime.now()-start
print(end, '秒')
