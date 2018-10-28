# author: bruwon
# date:2018-10-24
# 1.给任意列表，查找x元素是否在列表里面，若在返回1，不在返回0
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

# 2.给一个英文的纯文本，统计其中的单词出现的个数
print('*'*10,'find word in file','*'*10)
#构造一个200个单词的文本
listext = []
for i in range(200):
    englishtext = ''.join(random.sample(string.ascii_lowercase,5))
    listext.append(englishtext)
print(listext)#打印文本
#开始遍历查找并计数
count = 0 #计数器
textstr = 'engli'
for i in range(len(listext)):
    if listext[i] == textstr:
        count += 1
print('the word:{},appear:{}'.format(textstr,count))