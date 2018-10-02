
#就地修改
lst = [2, 4, 6, 4, 2, 3, 8, 3]

def sortedNewlist(num):

    num.insert(0, 0)

    for i in range(2, len(num)):
        if int(num[i]) >= int(num[i - 1]):
            continue
        else:
            num[0] = num[i]
            num[i] = num[i - 1]
            for j in range(i - 1):
                if int(num[0]) >= int(num[i - 2 - j]):
                    num[i - 1 - j] = num[0]
                    break
                else:
                    num[i - 1 - j] = num[i - 2 - j]
    num.pop(0)
    return num

print(sortedNewlist(lst))
print(id(lst))
print(id(sortedNewlist(lst)))



print('----------------分割线---------------------------------')
#创建一个新列表
lst1 = [5, 2, 4, 6, 4, 2, 3, 8, 3]


def NsortedNewlist(lst):

    num = [0]
    num.extend(lst)

    for i in range(2, len(num)):
        if int(num[i]) >= int(num[i - 1]):
            continue
        else:
            num[0] = num[i]
            num[i] = num[i - 1]
            for j in range(i - 1):
                if int(num[0]) >= int(num[i - 2-j]):
                    num[i - 1-j] = num[0]
                    break
                else:
                    num[i - 1-j] = num[i - 2-j]
    num.pop(0)
    return num


print(NsortedNewlist(lst1))


print('----------------分割线---------------------------------')
#创建一个新列表
lst2 = [5, 2, 4, 6, 4, 2, 3, 8, 3]


def NrsortedNewlist(lst, fn=lambda a,b:a <= b):

    num = [0]
    num.extend(lst)

    for i in range(2, len(num)):
        if  fn(int(num[i]), int(num[i - 1])):
            continue
        else:
            num[0] = num[i]
            num[i] = num[i - 1]
            for j in range(i - 1):
                if fn(int(num[0]),int(num[i - 2-j])):
                    num[i - 1-j] = num[0]
                    break
                else:
                    num[i - 1-j] = num[i - 2-j]
    num.pop(0)
    return num


print(NrsortedNewlist(lst2))
print(NrsortedNewlist(lst2,fn=lambda a, b:a >= b))
