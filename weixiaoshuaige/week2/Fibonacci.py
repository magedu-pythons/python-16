a = 1
b = 1
c = 0
print(a, b, sep = '\n')
while True:
    c = a + b
    if c >= 100:
        break
    print(c)
    a = b
    b = c