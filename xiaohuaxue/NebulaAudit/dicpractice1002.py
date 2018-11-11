
def add(x, y):
    return x+y

d = {'x':5, 'y':6}

c = add(*d.values())
e = add(*d.keys())
f = add(**d)
print(c)
print(e)
print(f)



import nodelist

chain = nodelist.ChainTable()
chain.append([1,2,3,4,5])
chain.append([1,2,3,4,5,6,7,8])
chain.append('hello world')
chain.insert(1,'xiaohuaxue')

print(chain.head,chain.head._next,chain.head)
print(chain)