t = ((('a'),('b')),(('c'),('d')))
print((lambda t: [dict(((t[0][x], t[1][x]),)) for x in range(len(t))])(t))


t1 = (('a'),('b'))
t2 = (('c'),('d'))
print((lambda *args: [dict((x,)) for x in zip(t1,t2)])(t1,t2))