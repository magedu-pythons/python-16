
x=1
y=1
z=0
print(x)
print(y)
while z<100:
    z=x+y
    x=y
    y=z
    if z<100:
        print(z)