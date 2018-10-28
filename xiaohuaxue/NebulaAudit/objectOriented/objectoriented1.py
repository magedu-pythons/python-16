
class Person:
    def eat(*args):
        print('我吃{}'.format(args))

class Fish:
    name = '鱼'


per = Person()

fi = Fish()
name = fi.name
per.eat(name)


