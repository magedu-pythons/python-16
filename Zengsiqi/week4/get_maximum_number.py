from random import randint
lst = []

for i in range(20):
    lst.append(randint(1,99))

print(lst)

for x in range(3):
    maxvalue = lst[x]
    subscript = 0
    for y in range(x+1,20):
        if lst[y] > maxvalue:
            maxvalue = lst[y]
            subscript = y
    if lst[x] < maxvalue:
        lst[subscript], lst[x] = lst[x], lst[subscript]

    print('times:{},max value:{}'.format(x,lst[x]))
