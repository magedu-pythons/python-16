# 实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。


# 封装为函数
def judge_substr(basestr:str, substr:str):
    for i, v in enumerate(basestr):
        # 找到相同的部位，对basestr进行切片判断
        if substr[0] == v and basestr[i:i+len(substr)] == substr:
            print('{}是{}的子串'.format(substr, basestr))
            if len(substr) == 1:    # 单个字符串打印输出
                return '首次出现在{}的索引为{}'.format(basestr, i)
            return '首次出现在{}的索引范围为{}-{}'.format(basestr, i, i+len(substr)-1)
    else:
        print('{}不是{}的子串'.format(substr, basestr))

# 测试
if __name__ == '__main__':
    str1 = 'abcdef'
    str2 = 'cde'
    print(judge_substr(str1, str2))



# 封装为类
class JudgeSubstr:
    def __init__(self, substr:str):
        self.substr = substr
        self.length = len(self.substr)

    def issubstr(self, basestr:str):
        for i, v in enumerate(basestr):
            if self.substr[0] == v and basestr[i:i + self.length] == self.substr:
                print('True')
                if self.length == 1:
                    return print('首次出现在{}的索引为{}'.format(basestr, i))
                return print('首次出现在{}的索引范围为{}-{}'.format(basestr, i, i+self.length-1))
        else:
            print('False')

# 测试
if __name__ == '__main__':
    str1 = 'abcdef'
    str2 = 'cde'
    string = JudgeSubstr(str2)
    string.issubstr(str1)



"""
(0 + 0)

   一个__name__就行  
"""