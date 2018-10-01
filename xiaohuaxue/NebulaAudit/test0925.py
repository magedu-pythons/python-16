# 给一个数，判断是否为质数
num2 = int(input('请输入一个数'))
pNum = 0
if num2 > 1:
    for i in range(2, num2):
        if num2 % i == 0:
            pNum = 1
            break
    if pNum == 1:
        print('不为质数1')
    else:
        print('为质数')
else:
    print('不为质数2')

#打印一个边长为n的正方形，用*号代表单位长度的起点与终点

n = int(input('输入要打印的正方形边长：'))

sepTop = '*'
sepMid = '*'

for i in range(n):
    sepTop += '\t*'
    sepMid += '\t'
else:
    sepMid += '*'
print(sepTop)

for i in range(n-1):
    print(sepMid)
else:
    print(sepTop)



