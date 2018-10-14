# author: bruwon
# date:2018-10-12
# for 
#练习一：打印质数2018-10-12
print(">>>质数，又名素数，除了1和它本身，没有其他因素的正整数！")

for i in range(1,100):
    if i<4: 
        print(i)
    if (not i%2==0) and (not i%3==0) and i!=1: 
        print(i)  
#练习二：打印20个斐波那契数列2018-10-13
print(">>>斐波那契数列，前两个数为1，从第三项开始，每个数等于前两项相加。")
a=1
b=1
c=0
print(a)
print(b)
for i in range(1,20):
    c=a+b
    a=b
    b=c
    print(c)