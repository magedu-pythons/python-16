

a = 0
b = 1
c = 0
print(b)
while c < 100:
    c = a + b
    if c > 100:
        break
    print(c)
    a = b
    b = c

print('我是分割线--------------------------------')
# 厉害的写法
a = 1
b = 1
print(a)
while b < 100:
    print(b)
    a, b = b, a+b

print('我是分割线--------------------------------')
a = 1
b = 1
count = 2
while True:
    count += 1
    if count > 101:
        break
    a, b = b, a + b
print(str(count - 1)+'项为：'+str(b))

print('我是分割线--------------------------------')
# 厉害的写法
a = 1
b = 1
for count in range(99):
    a, b = b, a + b
else:
    print(b)
