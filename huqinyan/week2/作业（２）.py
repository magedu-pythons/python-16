####��ӡ��100���ڵ�쳲��������У�ʹ��2�ַ���ʵ��
### ��һ�ַ���
list1 = [0,1]
while True:
    sum = list1[-1] + list1[-2]
    if sum>100:
        break
    list1.append(sum)
print(list1)


list1 = [0,1]
sum = 0
while sum<100:
    sum = list1[-1] + list1[-2]
    list1.append(sum)
list1.pop()
print(list1)

###�ڶ��ַ���

a = 1
b = 1
while b<100:
    print(b,end=' ')
    a,b =b,a+b


####ʹ�� Python ʵ��������� 200 ���ظ������루�����Ż�ȯ�����ַ������ȴ���5����
import random
a1 = 'abcdefghijklmnopqrstuvmsyz'
a2 = a1.upper()
a3 = '1234567890'*3
l = [a1,a2,a3]
for i in range(200):
    for j in range(6):
        a4 = random.randint(0,2)
        a5 = random.randint(0,25)
        print(l[a4][a5],end = ' ')
    print( )


"""

( □ )

    优惠码问题，没有考虑重复生成的处理
"""
