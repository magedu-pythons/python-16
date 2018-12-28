"""
本周作业来袭内容如下：（11.26-12.2）
1、# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
2、输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
"""
# 第一题
def fn(x,y):
    dt = {}
    lst = []
    for i in range(len(x)):
        dt = {x[i]:y[i]}
        lst.append(dt)
    return lst
print(fn(('a','b','c'),('d','e','f')))

func = lambda x, y:[dict((item,)) for item in zip(x, y)]
print(func((('a'),('b')), (('c'),('d'))))
print('~~~~~ second:str reversed~~~~~')
#第二题
strings = 'magedu python'
print('source strings: {}'.format(strings))
fnstr = lambda x: ' '.join(item for item in reversed(x.split()))
print('reversed strings: {}'.format(fnstr(strings)))





"""
(0 + 0)

    都做的不错！
"""