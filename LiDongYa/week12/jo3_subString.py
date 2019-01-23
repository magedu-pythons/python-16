'''
输入一个字符串，求不含有重复字母的最长子串的长度
例如：
   输入字符串'aaa'，其不含有重复字母的最长子串为‘a’，输出长度为1 
'''


def find_substring(src):
    start = 0
    lst = []
    for i in range(len(src) - 1):
        if src[i] == src[i + 1]:    # 当前后元素相同时，切片获取子串
            string = src[start:i + 1]
            if start == 0:
                lst.append(string)
            if len(string) > len(lst[0]):
                lst[0] = string     # 更新最长子串
            start = i+1             # 更新起步位置
    else:
        string = src[start:]
        if len(string) > len(lst[0]):
            lst[0] = string
    return len(lst[0])

if __name__ == '__main__':
    s = 'abbcdeffeg'
    print(find_substring(s))