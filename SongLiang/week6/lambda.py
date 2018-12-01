t = ((('a'),('b')),(('c'),('d')))
print((lambda t: [dict(((t[0][x], t[1][x]),)) for x in range(len(t))])(t))