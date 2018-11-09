
def fn2(n,lst=[0,1]):
    a = lst[len(lst)-1]+lst[len(lst)-2]
    if a > n:
        lst.pop(0)
        return lst
    else:
        lst.append(a)
    return fn2(n,lst)

print(fn2(10000000000000))
