"""
思路

1、规律：
    当n=2，即'()()','(())'
    当n=3时，即在上述组合的左单括号'('后边依次加一个'()',同时也在每个组合后加一个'()'
2、演示：
    对于'()()'
        组合左单括号加'()' ------>   '(())()', '()(())'
        后加括号          ------>   '()()()'
    对于'(())'
        组合左单括号加'()' ------>   '(()())', '((()))'
        后加括号          ------>   '(())()'	
3、结果去重
"""

def brackets_comb(count):
    if count == 1:  # base case
        value1 = {'()'}
        return value1

    value = set()   # set去重
    for item in brackets_comb(count - 1):     # 遍历上一次组合
        for i, val in enumerate(item):  # 遍历组合中的元素
            if val is '(':              # 如果是'('，后面插入'()'
                value.add('()'.join([item[:i+1], item[i+1:]]))
        value.add('()'+item)            # 对组合后面插入'()'
    return value


if __name__ == '__main__':
    count = int(input('>>>'))
    print(brackets_comb(count))