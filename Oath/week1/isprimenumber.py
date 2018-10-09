import datetime
number = 100000
count = 1
# 方法一
start = datetime.datetime.now()
for i in range(3, number+1, 2):   # 舍弃所有偶数
    for j in range(3, int(i**0.5)+1, 2):   # 上一步舍弃了偶数,奇数与偶数取模不为0,此处也须去掉偶数
        if i % j == 0:
            break
    else:
        count += 1
delta = (datetime.datetime.now() - start).total_seconds()
print(count)
print(delta)
print('~'*10)

# 方法一改进
count1 = 1
start = datetime.datetime.now()
for i in range(3, number+1, 2):  # 舍弃所有偶数
    uplimit = int(i**0.5)+1
    if i > 10 and i % 10 == 5:    # 大于10且尾数为5的数为合数
        continue
    for j in range(3, uplimit, 2):   # 上一步舍弃了偶数,奇数与偶数取模不为0,此处也须去掉偶数
        if i % j == 0:
            break
    else:
        count1 += 1
delta = (datetime.datetime.now() - start).total_seconds()
print(count)
print(delta)
print('~'*10)

# 方法二
import math
start = datetime.datetime.now()
lst = [2]   # 列表：用于存放找到的素数
count_new = 1
for i in range(3, number, 2):
    flag = False
    n = math.ceil(math.sqrt(i))
    for j in lst:  # 引入素数列表,一个合数能分解为几个素数的乘积
        if i % j == 0:
            flag = False
            break
        if j >= n:
            flag = True
            break
    if flag:
        count_new += 1
        lst.append(i)
delta = (datetime.datetime.now() - start).total_seconds()
print(count_new)
print(delta)
print('~'*10)

# 方法三
# 大于5的素数一定和6的倍数相邻
start = datetime.datetime.now()
count_thirt = 2
for i in range(4, number):
    if i % 6 != 1 and i % 6 != 5:  # # 大于5的素数与6的倍数相邻1或5
        continue
    else:
        sum = int(i**0.5)+1
        for j in range(5, sum, 2):
            if not i % j:
                break
        else:
            count_thirt += 1
            pass
delta = (datetime.datetime.now() - start).total_seconds()
print(count_thirt)
print(delta)
print('~'*10)

# 方法4：质数筛法
start = datetime.datetime.now()
count_fourth = 0
flagLst = [True]*(number+1)  # 标记列表：是合数就记为False.n+1个是方便数字与所引对齐
flagLst[0] = flagLst[1] = False
for i in range(2, int(number**0.5)+1):
    if not flagLst[i]:
        continue
    for j in range(i*i, number+1, i): # 如果i是素数，则i的倍数都不是素数
        flagLst[j] = False
count_fourth = [i for i in range(len(flagLst)) if flagLst[i]]
delta = (datetime.datetime.now() - start).total_seconds()
print(len(count_fourth))
print(delta)
print('~'*10)