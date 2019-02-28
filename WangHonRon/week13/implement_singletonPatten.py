# 1、python 中如何实现单例模式，尽可能多的写出实现方式

# 在Python中模块变量本身是单例形式

# 什么是单例模式：
# 1. 单例模式，是一种常用的软件设计模式。
# 2.在它的核心结构中只包含一个被称为单例的特殊类。
# 3.通过单例模式可以保证系统中，应用该模式的一个类只有一个实例。即一个类只有一个对象实例



class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# test
sing1 = Singleton()
sing2 = Singleton()

print(id(sing1), id(sing2))


# use decator
def singleton(cls):
    _instance = {}

    def wrap():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return wrap


# test

@singleton
class A:
    pass


a1 = A()
a2 = A()
print(id(a1), id(a2))