
class Node(object):
    def __init__(self, data, pnext = None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        return str(self.data)

class ChainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

#判断链表是否为空
    def isEmpty(self):
        return (self.length == 0)

#在链表尾部增加节点数据
    def append(self,dataOrNode):
        item = None
        if isinstance(dataOrNode,Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if self.head == None:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:      #循环为空时，停止循环，直接在这个位置赋值增加节点数据，最后一个节点的_next为空
                node = node._next
            node._next = item      #上面循环为空时，停止循环，直接在这个位置赋值增加节点数据，最后一个节点的_next为空
            self.length += 1

#删除节点
    def delete(self,index):
        if self.isEmpty():
            print('链表为空，无删除对象')
            return

        if index < 0 or index > self.length - 1:
            print('索引超界，无法删除对象')
            return

        if index == 0:
            self.head = self.head._next
            self.length -= 1

        else:
            node = self.head
            for i in range(index-1):
                node=node._next
            node._next = node._next._next
            self.length -= 1

#修改节点数据
    def update(self, index, data):
        if self.isEmpty():
            print('链表为空，无修改的对象')
            return

        if index < 0 or index > self.length - 1:
            print('索引超界，无法修改对象')
            return

        if index == 0:
            self.head.data = data
        else:
            node = self.head
            for i in range(index):
                node = node._next
            node.data = data

#获取索引节点数据GetItem()
    def getItem(self,index):
        if self.isEmpty():
            print('链表为空，无获取的对象')
            return

        if index < 0 or index > self.length - 1:
            print('索引超界，无法获取对象')
            return

        if index == 0:
            return self.head.data
        else:
            node = self.head
            for i in range(index):
                node = node._next
            return node.data

#获取节点数据的索引号GetIndex()
    def getIndex(self,data):
        if self.isEmpty():
            print('链表为空，无获取的对象的索引')
            return

        flag = []

        if data == self.head.data:
            flag.append(0)

        node = self.head
        for i in range(1, self.length):
            node = node._next
            if node.data == data:
                flag.append(i)

        if flag:
            return flag
        else:
            print('链表内无此数据')
            return

#插入数据insert()
    def insert(self, index, data):
        if self.isEmpty():
            print('链表为空，无获取的对象')
            return

        if index < 0 or index > self.length - 1:
            print('索引超界，无法获取对象')
            return
        #找到index-1的_next赋值与data
        #eval(repr(obj))
        item = None
        if isinstance(data,Node):
            item = data
        else:
            item = Node(data)

        temp = self.head
        if index == 0:
            self.head = item
            self.head._next = temp
            self.length += 1
        else:
            node = self.head
            for i in range(1,index):
                node = node._next
            temp1 = node._next
            node._next = item
            node._next._next = temp1
            self.length += 1
        #找到index+1的node赋值与index的_next




chain = ChainTable()
print(chain.__class__)
print(chain.__dict__)
print(chain.__class__.__name__)
chain.append([1,2,3,4])
chain.append((11,22,33,44))
print(chain.__dict__)
print(ChainTable.__dict__)

a = ChainTable()
a.append([1,2,3,4])
a.append((11,22,33,44))
a.append('hello world!')
print(a.__dict__['head'])
print(a.__dict__['length'])
a.__class__.__dict__['append'](a,'xiaohuaxue')
print(a.__dict__['length'])
ChainTable.__dict__['append'](a,{'x':1,'y':2})
print(a.length)
a.name = 'xiaohuaxue'
print(a.__dict__)
a.__dict__.__delitem__('name')
print(a.__dict__)