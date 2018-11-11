#first 判断回文数
def pdnum(num):
    num_s = reversed(str(num))
    temp = 0
    tag = [i for i in range(len(str(num)),0,-1)]
    dict_num = {i:int(v) for i,v in zip(tag,list(num_s))}

    for i,v in dict_num.items():
        n = 1
        for j in range(i-1):
            n*=10
        temp += n*v

    if num == temp:
        return True
    else:
        return False

#second 判断回文数
def pdnum2(num):
    num_s = reversed(str(num))
    num_l = ''
    for c in num_s:
        num_l += c

    if num == int(num_l):
        return True
    else:
        return False

print(pdnum(123321))
print(pdnum(11112))
print('----------分界线-----------------')
print(pdnum2(123321))
print(pdnum2(11112))