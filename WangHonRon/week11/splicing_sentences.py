# 3、根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子:
# 例如: 输入一个字符串："thisisanexample", 程序输出: "this is an example"


def word_break(inputs: str, word_set: set, memorized: dict):

    if inputs in memorized:
        return memorized[inputs]
    res = []
    if len(inputs) == 0:
        return res
    if inputs in word_set:
        res.append(inputs)
    for i in range(1, len(inputs)):
        word = inputs[:i]
        if word not in word_set:
            continue
        suffix = inputs[i:]
        segmentions = word_break(suffix, word_set, memorized)
        for segmention in segmentions:
            res.append(word + ' ' + segmention)

    memorized[inputs] = res
    return res


# test
ins = 'thisisanexample'
sd = {'this', 'is', 'an', 'example', }
d = {}
print(word_break(ins, sd, d))