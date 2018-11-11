import copy
import datetime

def factorial(num):
    result = 1
    if not (num == 0 or num == 1):
        for i in range(2,num+1):
            result *= i
    return result

def factorial2(num1, num2):
    delta_num = abs(num1 - num2)
    temp = [num1,num2,delta_num]
    temp.sort()
    flag_min= 1
    flag_mid= 1
    flag_max= 1
    result = 1
    if not (temp[0] == 0):
        for i in range(1,temp[2]+1):
            result *= i
            if i == temp[0]:
                flag_min = result
            if i == temp[1]:
                flag_mid = result
            if i == temp[2]:
                flag_max = result
    result=flag_max//(flag_min*flag_mid)
    return result




        # return result


start = datetime.datetime.now()

for i in range(100):
    num = []
    temp = 0
    temp1 = []

    if not (i % 2 ==0):
        c = int((i+1)/2)
    else:
        c = int((i + 1) / 2 + 1)

    for j in range(c):
        # temp = factorial(i) / (factorial(j)* factorial(i - j))
        temp = factorial2(i,j)
        num.append(temp)

    if not(i % 2 == 0):
        temp1 = copy.deepcopy(num)
        temp1.reverse()
    else:
        temp1 = copy.deepcopy(num)
        temp1.reverse()
        temp1.pop(0)

    num += temp1
    print(num)

end = datetime.datetime.now() - start

print(end)

print(factorial2(0,0))