from random import randint

num = randint(10000,99999)
print(num)

num = str(num)
a,b,_,c,d = num
if a==d and b==c:
    print("The number {} is palindromic number".format(num))
else:
    print("The number {} is not palindromic number".format(num))