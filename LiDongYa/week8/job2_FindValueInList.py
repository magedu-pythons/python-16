# 给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11


def listvalue4sum(src:list, number:int):
    flag = False
    for i in range(len(src)):  
        for j in range(i, len(src)):    
            if lst[i] + lst[j] == number:    # 依次遍历元素，相加判断
                flag = True
                print("{} 和 {} 的和为 {}".format(lst[i], lst[j], number))
    if not flag:
        print("列表中不存在两个数的和为{}".format(number))

lst = [1, 5, 2, 7, 4, 9]
listvalue4sum(lst, 11)