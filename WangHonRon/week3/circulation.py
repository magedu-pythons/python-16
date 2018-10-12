# author: bruwon
# date:2018-10-12
# for 
#练习一：打印质数
print(">>>质数，又名素数，除了1和它本身，没有其他因素的正整数！")

for i in range(1,100):
    if i<4: 
        print(i)
    if (not i%2==0) and (not i%3==0) and i!=1: 
        print(i)  