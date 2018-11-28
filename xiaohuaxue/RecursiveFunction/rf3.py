

def foo(n):
    return 1 if n < 2 else foo(n-1) + foo(n-2)

print(foo(100))


