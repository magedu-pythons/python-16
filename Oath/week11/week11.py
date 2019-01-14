# 23、实现数据结构stack(栈)，并实现它的append，pop方法【动手查询相关资料理解stack特点以及与queue区别】
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def __repr__(self):
        return f'{self.item}'


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None

    def __iter__(self):
        current = self.bottom
        while current:
            yield current
            current = current.next

    def append(self, item):
        item = Node(item)
        if self.top is None:
            self.bottom = item
        else:
            self.top.next = item
        self.top = item
        return self

    def pop(self):
        current = self.bottom
        while current.next is not self.top:
            current = current.next
        self.top = current
        tmp, current.next = current.next, None
        return tmp


stack = Stack()
stack.append(5).append(6).append('abc').append('87883')
print(stack.pop())
print(stack.pop())


#
# 24、打印出N对合理的括号组合。例如： 当N=3，输出：()()(),()(()),(())(),((())),(()())

# 深度优选与广度优先

def print_parenthesis(pairs, open, close, ans=''):
    if open == pairs and close == pairs:
        print(ans)
    if open < pairs:
        print_parenthesis(pairs, open + 1, close, ans + '(')
    if open > close:
        print_parenthesis(pairs, open, close + 1, ans + ')')

print_parenthesis(3, 0, 0)


# 25、根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子:
# 例如: 输入一个字符串："thisisanexample", 程序输出: "this is an example"
class WordHandle:
    cache = {}

    def __init__(self):
        self.ans = ''

    def handle(self, m_str, word):
        if m_str is None:
            return None
        start = 0
        for i in range(len(m_str)):
            if m_str[start:] in self.cache:
                self.ans += self.cache[m_str[start:]]
                break
            elif m_str[start:i + 1] in word:
                self.ans += (m_str[start:i + 1] + ' ')
                start = i + 1
        self.ans = self.ans.rstrip()
        self.cache[m_str] = self.ans
        return self.ans


word_set = {'this', 'is', 'an', 'example'}
test_str = "thisisanexample"
wh = WordHandle()
print(wh.handle(test_str, word_set))