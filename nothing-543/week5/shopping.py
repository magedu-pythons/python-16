import random
def shop():
    '''
    1..  袜子
    2..  鞋子
    3..  拖鞋
    4..  项链
    '''
    num = random.randint(1, 100)
    print(num)
    if num < 11:
        return 1   #袜子
    elif num < 31:
        return 2   #鞋子
    elif num < 61:
        return 3   #拖鞋
    else:
        return 4   #项链


"""
(0 + 0)

    参考答案实现
"""