
#可变位置参数
def add(*num):
    sum = 0
    for i in num:
        sum += i
    return sum

b = add(1,2,6,9,15,69,5486,4685,56)
print(b)

#可变关键字参数
def showconfig(**kwargs):
    for k,v in kwargs.items():
        print('{} = {}'.format(k,v))

showconfig(host='127.0.0.1',port='8080',username = 'xiaohuaxue', password = '123456')

#混合参数
def variableparameter(*args,x,y,**kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
    print(type(kwargs))

variableparameter(3,5,x=3,y=8,a='hello world',b='www')

#特殊写法,强制关键字输入实参
def fn(*,x,y):
    print(x,y)

fn(x=3,y=4)

def fn1(z,*,x,y):
    print(x,y,z)

fn1('hello world',x=3,y=4)

def fn2(*args,x=5):#一般keyword的参数都是给默认值即缺省值
    print(x)
    print(args)

fn2(3,4)
fn2(5)
