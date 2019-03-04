t = ((('a'),('b')),(('c'),('d')))
print((lambda t: [dict(((t[0][x], t[1][x]),)) for x in range(len(t))])(t))


t1 = (('a'),('b'))
t2 = (('c'),('d'))
print((lambda *args: [dict((x,)) for x in zip(t1,t2)])(t1,t2))

"""
(0 + 0)
    
    不要以python的模块名和关键字命名文件名
"""