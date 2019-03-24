#print Fibonacci queue within 100
#The first solution to print Fibonacci queue within 100
a1 = 0
a2 = 1
print('{}\n{}{},{}'.format('The first solution result is','The Fibonacci queue within 100 is:',a1,a2),end=',')
flag = True
while flag:
    Fibo = a1 + a2
    if Fibo <= 100:
        print(Fibo,end=',')
        a1 = a2
        a2 = Fibo
    else:
        flag = False
#The second solution to print Fibonacci queue within 100
Fibo = [0,1]
while True:
    n = Fibo[-1] + Fibo[-2]
    if n <= 100:
        Fibo.append(n)
    else:
        break
print('\n{}\n{}{}'.format('The second solution result is','The Fibonacci queue within 100 is:',Fibo))
print('\n{}'.format('~~~~~~~~~~~~~~~~~~'))
#print 200 random activation codes
import random
lst = list(range(10**4,10**5))
print('{}\n{}'.format('The 200 random activation codes are(made by numbers):',random.sample(lst,200)))

#print 200 random activation codes
lst = ['a','b','c','d','e','A','B','C','D','E','1','2','3','4','5']
print('The 200 random activation codes are(made by letters and numbers):')
from random import choice
for i in range(200):
    for j in range(5):
        print(choice(lst),end='')
    print(',',end='')

