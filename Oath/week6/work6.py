# 9、现有两元组('a', 'b'),('c', 'd'),请使用匿名函数生成列表[{'a':'c'},{'b':'d'}]
#
target = list(map(lambda x, y: {x: y}, ('a', 'b'), ('c', 'd')))
print(1, target)
#
fst = ('a', 'b')
scd = ('c', 'd')
target = lambda x, y: [{x[i]: y[i]} for i, val in enumerate(x if len(x) <= len(y) else y)]
print(2, target(fst, scd))
target = lambda: [{item[0]: item[1]} for item in zip(('a', 'b'), ('c', 'd'))]
print(3, target())
# 10、输入一个英文句子，翻转句子中的单词顺序，但单词内字符的顺序不变
line = '''It has been a while between books, I know. So a reminder may be in order.'''
def word_reverse(line: str):
    word = line.split()
    sline = ''
    for i in range(len(word)):
        sline += ' {}'.format(word[-i-1])
    return sline
print(word_reverse(line))
print('='*20)
#
target = lambda line:' '.join(line.split()[::-1])
print(target(line))
print('='*20)
#
import re
def word_reverse(line:str):
    regex = re.compile('[^\w]')
    word = regex.split(line)
    return ' '.join(word[::-1])
print(word_reverse(line))