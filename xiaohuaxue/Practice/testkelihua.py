
#z=f(x,y)
def add(x,y):
    return x+y
print(add(3,2))

#柯里化
#z=f(x)(y)
def new_add(x):
    def inner(y):
        return x+y
    return inner
print(new_add(3)(2))
