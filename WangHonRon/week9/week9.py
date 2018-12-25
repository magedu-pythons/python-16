'''
第九周作业班主任-薇薇 12月17号 星期一 13:58
各位小伙伴又到了写作业的时候了哦，小伙伴们加油了哦~~
本周作业小伙伴看这里：
1、请实现函数 new_counter ，使得调用结果如下：
      c1 = new_counter(10)
      c2 = new_counter(20)
      print（c1(), c2(), c1(), c2()）
      outputs ：
      11 21 12 22
2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符
'''
#No.1
def new_counter(num):
    temp = 0

    def wrapper():
        nonlocal temp
        temp += 1
        # num += temp
        # ret = fn(num)
        return num + temp
    return wrapper

# @cache
# def new_counter(num):
#
#     return lambda num : num

c1 = new_counter(10)
c2 = new_counter(20)
print(c1(),c2(),c1(),c2())

#No.2
def findrepeat():
    strs = input(">>>")
    lens = len(strs)
    if lens > 0:
        for i, item in enumerate(strs):
            if item  in strs[i+1:]:
                print("'{}' in '{}'' is repetition".format(item,strs))
                break
        else:
            print("'{}'' no repeat char".format(strs))


findrepeat()

