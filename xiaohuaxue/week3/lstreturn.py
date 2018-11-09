
#给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
def lstr(x,lst):
    for i in lst:
        if i == x:
            return 1
    else:
        return 0

print(lstr(66,[1,2,3,4]))

#任一个英文的纯文本文件，统计其中的单词出现的个数
import  re
def opentest(path):
    with open(path,'r') as f:
        lst = f.read().strip().split()
        temp = []
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lst[i][j] == '.' :
                    temp.append(lst[i])
                    break
                elif lst[i][j] =='!':
                    temp.append(lst[i])
                    break
                elif lst[i][j] == ',':
                    temp.append(lst[i])
                    break
                elif lst[i][j] == ':':
                    temp.append(lst[i])
                    break
                elif lst[i][j] == ';':
                    temp.append(lst[i])
                    break

        count = len(lst) - len(temp)

        for c in temp:
            lst_c = re.split('[!,.:;]',c)
            for k in range(len(lst_c)):
                if lst_c[k] == '':
                    lst_c.pop(k)
            count += len(lst_c)

    return count


print(opentest("/ghub/python-16/python-16/xiaohuaxue/week3/test"))