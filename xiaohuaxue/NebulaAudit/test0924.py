a = input("请输入一个不超过5位的正整数：")
b = len(a)
print('输入的直为' + str(b) + '位数')
for i in range(b):
    print(a[i])
print('测试成功')
for i in range(b - 1, -1, -1):
    print(a[i])
print('测试成功')

#用整除 //  余除 方式解题
number = int(a)
for i in range(b):
    val1 = number // 10
    val2 = number - val1 * 10
    print(val2)
    number = val1
print('测试成功')

#打印一个边长为n的正方形，用*号做边长单位，一个*为一个长度单位
n = int(input('请输入正方形边长'))
sign1 = '*'
sign2 = ' '
for i in range(n):
    if i == 0 or i == n-1:
        print(sign1*n)
    else:
        print(sign1+sign2*(n-2)+sign1)

#求100内所有奇数的和
numSum = 0
for i in range(1,100,2):
    numSum += i
print(numSum)

#求1到5阶乘之和
num1 = 1
sum1 = 0
for i in range(1,6):
    num1 = i*num1
    sum1 += num1
print(sum1)


