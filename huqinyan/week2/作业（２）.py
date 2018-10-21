####打印出100以内的斐波那契数列，使用2种方法实现
### 第一种方法
list1 = [0,1]
while True:
    sum = list1[-1] + list1[-2]
    if sum>100:
        break
    list1.append(sum)
print(list1)


list1 = [0,1]
sum = 0
while sum<100:
    sum = list1[-1] + list1[-2]
    list1.append(sum)
list1.pop()
print(list1)

###第二种方法

a = 1
b = 1
while b<100:
    print(b,end=' ')
    a,b =b,a+b


####使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random
a1 = 'abcdefghijklmnopqrstuvmsyz'
a2 = a1.upper()
a3 = '1234567890'*3
l = [a1,a2,a3]
for i in range(200):
    for j in range(6):
        a4 = random.randint(0,2)
        a5 = random.randint(0,25)
        print(l[a4][a5],end = ' ')
    print( )
