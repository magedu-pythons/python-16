# 打印100以内的斐波那契数列
f1 = 0
f2 = 1
print(f1, f2, end=' ')
while True:
    f1, f2 = f2, f1 + f2
    if f2 > 100:
        break
    print(f2, end=' ')

# exp2
# while f2 < 100:
#     print(f2, end=' ')
#     f1, f2 = f2, f1 + f2

# exp3
# def fib(pre=0, cur=1, lst=[0, 1]):
#     pre, cur = cur, pre + cur
#     if cur > 100:
#         return cur
#     lst.append(cur)
#     fib(pre, cur)
#     return lst
# print(fib())

# for i in range(100):
#     f1, f2 = f2, f1 + f2
#     if f2 > 100:
#         break
#     print(f2, end=' ')
