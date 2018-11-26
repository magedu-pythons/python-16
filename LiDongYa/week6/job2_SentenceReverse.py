# 输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变 

# 方法一：内建函数应用
def sentence_reverse1():
	s = input('>>>')
	
	return ' '.join([i for i in reversed(s.split())])	# 运用split函数和reversed函数

print(sentence_reverse1())


# 方法二：遍历、切片
def sentence_reverse2():
    s = input('>>>')
    lst = []
    count = 0
    for i in range(-1, -len(s)-1, -1):		# 从尾部遍历，以空白字符为断点，取值
        if count == 0 and s[i] == ' ':		
            lst.append(s[i+1:])				# 第一次切片需要取到尾部
            count = i
        elif s[i] == ' ':
            lst.append(s[i+1:count])
            count = i
    else:
        lst.append(s[:count])				# 最后一次则取到头部
    return ' '.join(lst)

print(sentence_reverse2())