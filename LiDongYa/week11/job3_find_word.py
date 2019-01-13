
def find_word(src_str:str, dictionary:set):
    """
    :param src_str: 源字符串
    :param dictionary: 字典库
    :return: 组合后的string
    """
    lst = []
    start = 0

    for i in range(0, len(src_str) - 1):
        item = src_str[start:i]
        if item in dictionary:
            lst.append(item)
            start = i
    else:
        lst.append(src_str[start:])
    return ' '.join(lst)

if __name__ == '__main__':
    string = "thisisanexample"
    dictionary = {'this', 'is', 'an', 'example', 'the', 'hello'}  # 单词字典
    print(find_word(string, dictionary))