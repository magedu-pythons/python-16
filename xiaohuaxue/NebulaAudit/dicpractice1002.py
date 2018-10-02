
def add(x, y):
    return x+y

d = {'x':5, 'y':6}

c = add(*d.values())
e = add(*d.keys())
f = add(**d)
print(c)
print(e)
print(f)