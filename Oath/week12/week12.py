# 26、实现一个可迭代的类：

class IterA:

    def __init__(self):
        self.lst = []

    def __iter__(self):
        yield from self.lst


# 27、给出一个无序的整型列表，找出最长连续元素序列的长度。时间复杂度要求在线性时间内；
# 例如：[8, 1, 9, 3, 2, 4], 即输出长度为4

def max_sequence(lst):
    ans = 0
    d = set(lst)
    for i in lst:
        if i - 1 not in d:
            start = i
            while i in d:
                i += 1
            ans = max(ans, i - start)
    return ans


lst = [8, 1, 9, 3, 2, 4, 0, 1]
print(max_sequence(lst))


#
def max_sequence(lst):
    ans = 0
    cache = {}  # 存放遍历过的数及其连续序列的长度
    for i in sorted(lst):
        # [1, 2, 3, 5, 6, 7, 8, 9]
        left = cache.get(i - 1, 0)  # 如i=5, 需要到字典中找它前一个值4的序列长度
        ans = max(ans, left + 1)
        cache[i] = left + 1
    return ans

lst = [8, 1, 9, 3, 2, 4, 0, 1]
print(max_sequence(lst))


# 上方法需要对列表进行排序，然后再查找。若同时查找元素前后值的序列长度，则不需要排序

def max_sequence(lst):
    ans = 0
    d = {}
    for i in set(lst):  # 去重后遍历，重复元素在连续序列只算一个
        left = d.get(i - 1, 0)
        right = d.get(i + 1, 0)
        ans = max(ans, right + left + 1)
        d[i] = right + left + 1
        d[i - left] = right + left + 1
        d[i + right] = right + left + 1
    return ans


lst = [8, 1, 9, 3, 2, 4, 0, 1]
print(max_sequence(lst))


#
print('~~~~~~~~~~~~~~~~~~~~~~')

print('最长子串实现==================')
#


# 28、输入一个字符串，求不含重复字母的最长子串的长度

def max_length_sub(m_str, ans=0):
    length = len(m_str)
    for i in range(length):
        ans_s = set()
        for j in range(i, length):
            if m_str[j] in ans_s:
                break
            ans_s.add(m_str[j])
        ans = max(ans, len(ans_s))
    return ans


s_test = 'pwekwlq', 'abcabcabcabb', 'abcdefg', 'abba', 'aaaaa'

for s in s_test:
    print(max_length_sub(s))


#
print('~~~~~~~~~~~~~~~~~~~~')
#

# O(n)

def max_length_sub(m_str, ans=0, start=0):
    cache = {}  # 存放遍历过的字符及其索引
    for i, val in enumerate(m_str, 1):
        if val in cache and cache[val] > start:  # 出现重复字符，保证start只向后移动
            start = cache[val]
        cache[val] = i
        ans = max(ans, i - start)
    return ans

s_test = 'pwekwlq', 'abcabcabcabb', 'abcdefg', 'abba', 'aaaaa'

for s in s_test:
    print(max_length_sub(s))