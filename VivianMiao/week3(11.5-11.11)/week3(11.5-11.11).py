#Is this a palindrome number?
n = int(input('Is this a palindrome number?Enter a number from 11111 to 99999:')) #abcde
a = n // 10000
b = n // 1000 - a*10
e = n % 10
d = (n % 100) // 10
if a == e and b == d:
    print('Yes')
else:
    print('No')
print('~~~~~~~~~~~~~~~~~~~')
#randomly choose 20 numbers in a range and print the biggest 3 numbers
n = int(input('in what range would you like to randomly choose 20 numbers?Enter the biggest number：'))
import random
lst = random.sample(range(n),20)
print('The 20 random numbers are',lst)
lst.sort()
print('The three biggest numbers are',lst[-1],lst[-2],lst[-3])


