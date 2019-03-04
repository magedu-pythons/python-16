"""
3、输入一个字符串，求不含有重复字母的最长子串的长度
例如：
   输入字符串'aaa'，其不含有重复字母的最长子串为‘a’，输出长度为1
"""
def length_substr(s: str):
    length = len(s)
    start = 0
    max_len = 0
    dict_cache = {}
    for i in range(length):
        key_cache = s[i]

        if key_cache in dict_cache and dict_cache.get(key_cache) >= start:
            start = dict_cache.get(key_cache) + 1

        dict_cache[key_cache] = i
        max_len = max(max_len, i - start + 1)
    print(dict_cache)
    return max_len
print(length_substr('aabsddpoigtt'))