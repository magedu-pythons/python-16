
class new_counter:
    """
    请实现函数 new_counter ，使得调用结果如下：
      c1 = new_counter(10)
      c2 = new_counter(20)
      print（c1(), c2(), c1(), c2()）
      outputs ：
      11 21 12 22
    """
    def __init__(self, num):
        self.num = num
    def __call__(self):
        self.num = self.num + 1
        return self.num

c1 = new_counter(10)
c2 = new_counter(20)
print(c1(), c2(), c1(), c2())




d = {}
str1 = input(">>>")
def repeat(string):
    def _repeat(fn):
        ret = fn(string)
        for i in d.values():
            if i > 1:
                print("{} is repeat".format(string))
            else:
                print("{} Don't repeat".format(string))
            return ret
    return _repeat

@repeat(str1)  #add_dict = repeat(string)(add_dict)
def add_dict(string:str):
    """
    实现一个函数，输入字符串，判断该字符串是否不含有重复字符
    """
    for c in string:
        d[c] = d.get(c, 0) + 1







