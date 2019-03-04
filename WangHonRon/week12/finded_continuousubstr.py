"""
2、给出一个无序的整型列表，找出最长连续元素序列的长度，时间复杂度要求在线性时间内。
例如：
    输入：[8,1,9,3,2,4]，那么其最长连续序列是[1,2,3,4]，即输出长度为4
思路：
1.先将无序列表排序；2.遍历列表，连续相邻差1放进缓存列表；
"""
#参考写法
def finded_conti_substr(longstr: list):
    if not longstr:
        return 0

    #用集合去重存储
    newstr = set(longstr)

    max_num = 0

    # 参考了答案~_~
    for i in longstr:
        if i - 1 not in newstr:
            j = i
            while i in newstr:
                i += 1
            max_num = max(max_num, i - j)

    return max_num

print(finded_conti_substr([5,6,1,2,8,7,3,3]))