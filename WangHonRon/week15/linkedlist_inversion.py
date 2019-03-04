# 1、请实现一个方法将链表反转
# 举例：
# 链表a，有节点1->2->3->4  反转后为：4->3->2-1
# 概念：链表是一种物理存储单元上非连续、非顺序的存储结构，数据元素的逻辑顺序是通过链表中的指针链接次序实现的

class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):

        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

    def output_list(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()

    def reversed_iter(self):
        # 反转节点
        last = None
        current = self.head
        while current:
            next_node = current.get_next()
            current.set_next(last)
            last = current
            current = next_node
        self.head = last


# test
if __name__ == '__main__':

    lst = LinkedList()
    for i in range(5):
        lst.insert(i)
    lst.output_list()
    print('='*30)
    lst.reversed_iter()
    lst.output_list()