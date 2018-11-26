number = input('>>>输入一个数字')
lst = ','.join(number)
length = len(lst)
flag = 0
for i in range(length // 2 + 1):
    if lst[i] == lst[-i - 1]:
        flag += 1
if flag == length // 2 + 1:
    print('该数{}是回文数'.format(number))
else:
    print('该数{}不是回文数'.format(number))


"""
(0 + 0)

    学会使用函数封装代码！
"""