#第一题
(lambda x,y:[{x[i],y[i]} for i in range(2)])((('a'),('b')),(('c'),('d')))

#第二题
def rst(arg):
    l = arg.split()
    for i in range(len(l),0,-1):
        print(l[i-1],end=' ')

rst('hello world')


"""
(0 + 0)

    建议自己增加一些数据测试，测试正确性
"""