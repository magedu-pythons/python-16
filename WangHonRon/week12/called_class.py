"""
参考
实现可迭代类
思路：实现类的可迭代方法
"""
class IterCls:
    def __init__(self):
        self.dct = {}

    def __iter__(self):
        yield from self.dct.items()


# test
iter_cls = IterCls()
iter_cls.dct ={'姓名':'张三','年龄':'21','性别':'男'}
for k,v in iter_cls:
    print('{}:{}'.format(k,v))