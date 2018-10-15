# 法一
def fib(s):
    n, a, b = 0, 0, 1
    while n < s:
        print(a)
        a, b = b, a + b
        n += 1
fib(5)

# 法二，yield
def fib(s):
    n, a, b = 0, 0, 1
    while n < s:
        yield a
        a, b = b, a + b
        n += 1
for i in fib(5):
    print(i)

# 法三, list列表

def fib(s):
    n, a, b = 0, 0, 1
    l = []
    while n < s:
        l.append(a)
        a, b = b, a + b
        n += 1
    print(l)
fib(5)
