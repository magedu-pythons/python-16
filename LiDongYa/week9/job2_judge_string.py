# 实现一个函数，输入字符串，判断该字符串是否不含有重复字符


# 方法一，根据长度判断
def judge_str1(string: str):
    set_container = set()
    for s in string:
        set_container.add(s)
    if len(set_container) == len(string):
        print('字符串不含有重复字符')
    else:
        print('字符串含有重复字符')
		
		
		
# 方法二：遍历
def judge_str2(string):
    for i, s in enumerate(string):
        if s in string[i+1:]:
            print('字符串含有重复字符')
            break
    else:
        print('字符串不含有重复字符')


"""
(0 + 0)

    
"""