import datetime
def decorator(fn):
    def wrap(*args,**kwargs):  #包装函数
        #before
        print("args={},kwargs={}".format(args,kwargs))
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        print('添加一次，记录一次')
        # after
        stop = datetime.datetime.now() - start
        if stop.total_seconds() > 2:
            print("{} took {}s.".format(fn.__name__,stop.total_seconds()))
        else:
            print("So fast")
        return ret
    return wrap

@decorator # 这个格式等价于 下面的函数全部应用decorator装饰器包装，如：add = decorator(add)
def add(x,y):
    return x+y

print(add(3,6))

f = decorator(add)  #f 赋值一个装饰器函数
m = f(3,2)
print(m)
