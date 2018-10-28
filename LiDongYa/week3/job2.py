# 任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

with open('file_test.txt', 'r', encoding = 'utf-8') as f:
    s = f.read()                                # 打开文件，并读取文件
    result = re.findall('.*?(\w+).*?', s, re.S) # 利用正则匹配字符串中的单词，去掉标点符号
    d = dict.fromkeys(result, 0)                # 生成含有单词的字典，value为0，方便计数
    for char in result: 
        d[char] += 1                            # 遍历列表，计数单词出现的次数
print(d)