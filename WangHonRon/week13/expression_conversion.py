# 3、将逆转波兰式转化为中序表达式（自行查询逆波兰式、中序表达式相关资料）
# 举例: 输入 {"5", "8", "4", "/", "+"}，输出 "(5+(8/4))"
# 波兰表达式：波兰式是在通常的表达式中，二元运算符总是置于与之相关的两个运算对象之前，所以，这种表示法也称为前缀表达式
#

def gen_rpn(inp):
    if not inp:
        return
    n = len(inp)
    lst = []
    result = ''
    for i in range(n):
        s = inp[i]
        if s == '/' or s == '+' or s == '*' or s == '-':
            if result == '':
                result = result + lst.pop()
            first = lst.pop()
            result = "(" + first + s + result + ')'
        else:
            lst.append(s)
    print("source list:{}".format(inp))
    return result


# test

i1 = ["5", "8", "4", "/", "+"]
print(gen_rpn(i1))