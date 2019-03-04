
def fn(n):
    temp = 1
    temp *= n
    return temp*fn(n-1) if n > 1 else temp

print(fn(5))


def f00(n,lst=[0,1]):
    lst.append(1)
    
    return lst
