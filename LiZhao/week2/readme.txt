#安装pyenv
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
cat ~/.bash_profile
export PATH='/home/hans/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"


_____________________________________________________
#求100以内的斐波那契数列两种实现

l = [0]
x = 0
y = 1
while y < 100:
    l.append(y)
    x,y = y,x+y
print(l)

**********************

l = [0,1]
while True:
    l.append(l[-1]+l[-2])
    if l[-1] > 100:
        l.pop()
        break
print(l)
_____________________________________________________
#200个无重复激活码
import random
s1 = 'abcdefghijklmnopqrstuvwxyz'
s2 = s1.upper()
s3 = '0123456789'*3
l = [s1,s2,s3]
for i in range(200):
        count = random.randint(7,7)
        for j in range(0,count):
            ran1 = random.randint(0,2)
            ran2 = random.randint(0,25)
            print(l[ran1][ran2],end='')
        print()
