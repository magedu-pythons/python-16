# 实现一个可迭代的类

class IterExample:
    def __init__(self):
        self.lst = [1, 2, 3]

    def __iter__(self):
        return iter(self.lst)


if __name__ == '__main__':
    iterExam = IterExample()
    for item in iterExam:
        print(item)