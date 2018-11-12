# author: bruwon
# date:2018-10-24
# 1.给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
print('*'*10,'find elem x','*'*10)
listr = random.sample(string.ascii_letters,10)
elem = 'x'
print(listr)
for i in range(len(listr)):
    if elem not in listr:
        flag = 0
        break

    else:
        flag = 1
        break
print('elem:{},return:{}'.format(elem,flag))

# 2.任一个英文的纯文本文件，统计其中的单词出现的个数
print('*'*10,'find word in file','*'*10)
#
listext = []
for i in range(200):
    englishtext = ''.join(random.sample(string.ascii_lowercase,5))
    listext.append(englishtext)
print(listext)#
#
count = 0 #
textstr = 'engli'
for i in range(len(listext)):
    if listext[i] == textstr:
        count += 1
print('the word:{},appear:{}'.format(textstr,count))




"""
(0 + 0)

    参考答案实现
"""