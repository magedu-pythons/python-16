#第一题
import random
def dis(arg):
    for i in range(len(arg)):
        a = random.randint(0,len(arg)-1)
        b = random.randint(0,len(arg)-1)
        arg[a],arg[b] = arg[b],arg[a]
    print(arg)

alist = [1,2,3,4,5,6]
dis(alist)

#第二题
import random

def draw(arg):
    ret = []
    x = 0

    for i in arg.values():
        x +=i

    for k,v in arg.items():
        lt = []
        por = int(v / x * 10)
        lt.append(k)
        end = lt * por
        ret.extend(end)
    return random.choice(ret)

comm = {'袜子':10,'鞋子':20,'拖鞋':30,'项链':40}
draw(comm)
