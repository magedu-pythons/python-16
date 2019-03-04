
class MyClass:
    '''hello world hi'''
    X = 2

    def foo(self):
        print('text')
        return

    @classmethod #类方法
    def mtd(cls):
        print('{}.x={}'.format(cls.__name__,cls.X))

    @staticmethod #静态方法
    def staticmtd():
        print('my class')




print(MyClass)
print(MyClass.X)
print(MyClass.foo)
print(MyClass.__doc__)
print(MyClass.__dict__)
print(MyClass.__name__)
print(type(MyClass))

a = MyClass()
MyClass.mtd()
a.mtd()





