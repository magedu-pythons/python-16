#### һ��5λ�����ж����ǲ��ǻ�������
a1 = input('������һ��5λ�������ж��ǲ��ǻ�������')
count =0
while True:
    if len(a1) == 5:
       for i in range(len(a1)//2):
          if  a1[i] == a1[-i-1]:
               count += 1
       if count ==2:
            print('�ǻ�����')
       else:
            print('���ǻ�����')
       break
    else:
        a1 = input('������Ĳ���һ��5λ����������һ��5λ�������ж��ǲ��ǻ�������')
        continue


####�������20�����֣�����ɸѡ����������3����
import random
a2 = []
a1 = random.sample(set(range(50)),20)
a1.sort(key=int,reverse=True)
for i in range(3):
    a2.append(a1[i])
print(a2)

"""
(0 + 0)

   参考答案的封装和实现
"""

