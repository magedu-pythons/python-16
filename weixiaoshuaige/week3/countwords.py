import collections
import re
with open(r'C:\Users\wenzhe\Desktop\python-16\weixiaoshuaige\week3\test.txt', 'r') as f:
    word_list = []
    word_reg = re.compile(r'\w+')
    for line in f:
        line_words = line.split()
        word_list.extend(line_words)
        words_dict = dict(collections.Counter(word_list))
        for k, v in words_dict.items():
            print(k, v)