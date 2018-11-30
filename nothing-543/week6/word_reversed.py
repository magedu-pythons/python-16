

words = input('>>>>')

def logger(words):
    list = []
    start = 0
    for i, c in enumerate(words):
        if c == " ":
            if start <= i:
                list.append(words[start:i])
                start = i + 1
    else:
        list.append(words[start:])
    def _logger(func):
        ret = func(list)
        print(" ".join(ret))
        return ret
    return _logger

@logger(words)  # re_words = logger(words)(re_words)
def re_words(lst):
    list_word = list(reversed(lst))
    return list_word





