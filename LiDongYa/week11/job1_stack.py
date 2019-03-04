class Stack:
    def __init__(self):
        self.items = []

    def append(self, item): # 添加元素
        self.items.append(item)
        return self.items   # 可实现连续添加

    def pop(self):  # 删除顶端元素
        return self.items.pop()

    def top(self):  # 获取顶端元素，但不删除
        return self.items[-1]

    def size(self): # 长度
        return len(self.items)

    def is_empty(self): # 是否为空
        return self.size() == 0