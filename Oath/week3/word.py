import string
from collections import OrderedDict
def word_count(file):
    with open(file, 'r') as f:
        test = f.read().split()
        m_chars = string.punctuation   # ascii中所有常用标点符号
        word_dict = OrderedDict()    # OrderedDict
        # count_dict = {}
        for i in test:
            word = i.strip(m_chars)    # 去掉字符串两端的标点符号
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict
print(word_count('word.txt'))