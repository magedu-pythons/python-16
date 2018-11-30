# 问题描述：一个5位数，判断它是不是回文数。
def palnumber(number):
    length = len(number)
    for i in range(length//2):
        if number[i] == number[-i-1]: # 利用字符串索引进行比较
            continue
        else:
            print('{}不是回文数'.format(number))
            break
    else:
        print('{}是回文数'.format(number))
    
palnumber(input('please input number:'))

"""
(0 + 0)


"""