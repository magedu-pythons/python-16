import random, copy
low = int(input('give me a lower'))
upp = int(input('give me a upper'))
lst = [0] * 20
for i in range(20):
    lst[i] = random.randint(low,upp)
print(lst)
lst2 = copy.copy(lst)
lst1 = [0] * 3
for j in range(3):
    maxnum = 0
    for n in range(len(lst2)):
        if maxnum > lst2[n]:
            continue
        else:
            maxnum = lst2[n]
            index = n
    lst2[index] = 0
    lst1[j] = index
for i in lst1:
    print(lst[i])
    #print(maxnum)
    #lst.remove(maxnum)


"""
(0 + 0)

    实现的太过于繁琐，可以更加精简
"""