n=int(input("Please enter a number: "))
a = 0
b = 1
print(0)
count = 0
for i in range(1,n+1):
    if a > n:break
    a,b=b,a+b
    print(a)


n=int(input("Please enter a number: "))
print(0)
print(1)
a = 0
b = 1
while True:
    c = a+b
    if c > n:break
    a = b
    b = c
    print(c)