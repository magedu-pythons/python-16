a = 0
b = 1
s = 0
print(b)

for i in range(100):
    s = a+b
    a,b = b,s
    if s<=100:
        print(s)
    else:
        break