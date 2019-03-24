class People():
    name = 'jerry'  # 公有的类属性
    __age = 18  # 私有的类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.__age = age  # 实例属性


p = People('tom',21)
p.name  # tom
People.name

print(p.name,People.name)