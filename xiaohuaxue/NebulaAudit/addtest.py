
def fDecorator(fn):
    def encapsulation(*args,**kwargs):
        #before
        print('测试成功！')
        ret = fn(*args,**kwargs)
        #after

        return ret
    return encapsulation


@fDecorator
def add(*args):
    sub = 0
    for i in args:
        sub += i
    return sub

a = add(3,3,4,5,6,*[1,*[2,2,5],5,69],*{'x':1,'y':2}.values())

print(a)

