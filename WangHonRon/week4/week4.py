# bruwon
# 2018-11-9
#1、问题描述：一个5位数，判断它是不是回文数。
# “回文”是指正读反读都能读通的句子,如“我为人人，人人为我”等
# 设n是一任意自然数。若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数。例如，若n=1234321，则称n为一回文数；但若n=1234567，则n不是回文数. 
n = input('>>>')
lenth = len(n)
count_iter = 0 
count_flag = 0
flag = False
for i in range(lenth):
    count_iter += 1
    if n[i] == n [-i-1]:
        count_flag += 1
        print('n[i] is {},n[-i-1] is {}'.format(n[i],n[-i-1]))
        flag = True
        continue
    else:
        flag = False
        break
print('{0} is {1},{2}count_iter:{3},{4}count_flag:{5}'.format(n,flag,'\n',count_iter,'\n',count_flag))
#2、随机生成20个数字，并且筛选出其中最大的3个数
import random
lst = [ random.randint(1,50) for i in range(20)]
nums = lst.copy()
length = len(nums)
print('resourse list:{}{}copy list:{}'.format(lst,'\n',nums)) 

for i in range(0,length):
    for j in range(0,length-1):
        
        if nums[j] > nums[j + 1]:
            nums[j],nums[j + 1] = nums[j + 1], nums[j]
                       
print('sorted list :{}'.format(nums))
print('three elem of max:{}'.format(nums[-3:]))