# author: bruwon
# date:2018-10-24
# 1.�������б�����xԪ���Ƿ����б����棬���ڷ���1�����ڷ���0
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

# 2.��һ��Ӣ�ĵĴ��ı���ͳ�����еĵ��ʳ��ֵĸ���
print('*'*10,'find word in file','*'*10)
#����һ��200�����ʵ��ı�
listext = []
for i in range(200):
    englishtext = ''.join(random.sample(string.ascii_lowercase,5))
    listext.append(englishtext)
print(listext)#��ӡ�ı�
#��ʼ�������Ҳ�����
count = 0 #������
textstr = 'engli'
for i in range(len(listext)):
    if listext[i] == textstr:
        count += 1
print('the word:{},appear:{}'.format(textstr,count))




"""
(0 + 0)

    参考答案实现
"""