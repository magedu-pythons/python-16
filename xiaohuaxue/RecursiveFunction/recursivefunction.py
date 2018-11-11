def fn(n):
    temp = 1
    for i in range(1,n+1):
        temp *= i
    return temp

print(fn(3))



def foo():
    t = 1
    def inner():
        nonlocal t
        t +=1
        return t
    return inner
f = foo()
print(f(),f(),f())