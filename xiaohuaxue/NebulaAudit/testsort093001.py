import datetime
import random
a = []
for c in range(10000):
    rand = random.randint(0, 10000)
    a.append(rand)
start = datetime.datetime.now()
b = []
s = 0
flag = 0
flagbool = False
for i in range(len(a)):
    for j in range(len(a)):
        if s >= int(a[j]):
            continue
        else:
            s = int(a[j])
            flag = j
            flagbool = True
    if not flagbool:
        break
    print(s)
    b.append(s)
    s = 0
    a.pop(flag)
end = datetime.datetime.now() - start
print(end, '秒')
a = b
print(a)
print(b)