

def countpr(base):
    def inc(tep = 1):
        nonlocal base
        base += tep
        return base
    return inc


foo =countpr(5)


f1 = countpr(5)
f2 = countpr(5)

print(foo(),f1(),f2())

print(id(foo),id(f1),id(f2))
