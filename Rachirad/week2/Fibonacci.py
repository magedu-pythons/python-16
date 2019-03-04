#!/usr/bin/env  python
#_*_conding: UTF-8_*_
#fileName=Fibonacci.py
"""the  Second week test
1 打印100以内斐波那契数列，使用二种方法实现

斐波那契数列:指像数列 0, 1, 1, 2, 3, 5, 8, 13,规律是：第0项是0，第1项是第一个1。而从第三项（1）开始，每一项都等于前两项（如第三项1=0+1）之和到第13项停止。
"""
#初始化第一，第二项
n1 = 0
n2 = 1
print ("斐波那契数列:")
print(n1)
print(n2)
count = 2
while count < 13:
    
    sum=  n1 + n2 
    if sum >100: break
    n1 = n2
    n2 = sum  
    count += 1
    print (sum)

#way2
"""
直接由公式F(n)=F(n-1)+F(n-2)（n>=0）项得出
F（0）=0,F(1)=1,
"""
m1=0
m2=1
print ("斐波那契数列")
print (m1)
print (m2)

for Sum in range(10) :
    Sum=m1+m2

    m1=m2
    m2=Sum
    print(Sum)
    
