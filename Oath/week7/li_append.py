# 14、以下代码输出什么，请解释原因
li = [[]] * 5
li[0].append(10)
print(li)
# [[10], [10], [10], [10], [10]]
'li中元素[]是可变类型用乘法获得, 这些元素为引用类型，其地址一样，当其中一个元素发生变化，其余元素也发生变化'
li[1].append(20)
print(li)
# [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
li.append(30)
print(li)
# [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
'此处是为li追加元素，该元素是一个不可变类型/字面常量'
#
def test(x, li=[]):
    for i in range(x):
        li.append(i**2)
    print(li)
test(3) # -> [0, 1, 4]
test(3, [100,200,300])  #  -> [100, 200, 300, 0, 1, 4]
test(1)   # [0, 1, 4, 0]
#
'__default__用元组保存了li的默认值,这个值并不会随函数体调用而发生改变(我在这理解的是这个默认值的地址不变化, ' \
'相当于这个元组存的是默认值的地址)，但li是可变类型，li中元素发生变化不会引起li地址的变化(即容器内部的东西变化不会引起容器位置的变化)'
#