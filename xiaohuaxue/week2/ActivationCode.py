
import random

#第一种
temp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ware = set()
while len(ware) < 200:
    codestr = ''
    for i in range(10):
        codestr += random.choice(temp)
    ware.add(codestr)

for c in ware:
    print(c)

print('--------------------------------------我是分割线-----------------------------------')
#第二种
import string
ware1 = set()
while len(ware1) < 200:
    ware1.add(''.join(random.sample(string.ascii_letters+string.digits,10)))

for c in ware1:
    print(c)