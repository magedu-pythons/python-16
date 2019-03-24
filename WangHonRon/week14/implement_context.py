# 2、上下文管理是什么？请实现一个python 类，具有上下文管理功能
# python 上下文，具有__enter__和__exit__属性

class A:
    def __init__(self, name='jerry'):
        self.name = name
        print('__init__:',self.name)

    def __enter__(self):
        print('__enter__:',self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__:',self.name)


with A() as a:
    print("========")