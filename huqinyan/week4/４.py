#### 一个5位数，判断它是不是回文数。
a1 = input('请输入一个5位数，来判断是不是回文数：')
count =0
while True:
    if len(a1) == 5:
       for i in range(len(a1)//2):
          if  a1[i] == a1[-i-1]:
               count += 1
       if count ==2:
            print('是回文数')
       else:
            print('不是回文数')
       break
    else:
        a1 = input('你输入的不是一个5位数，请输入一个5位数，来判断是不是回文数：')
        continue


####随机生成20个数字，并且筛选出其中最大的3个数
import random
a2 = []
a1 = random.sample(set(range(50)),20)
a1.sort(key=int,reverse=True)
for i in range(3):
    a2.append(a1[i])
print(a2)