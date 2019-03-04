import random
lst = [random.randint(1, 100) for _ in range(20)]
lst1 = sorted(lst)
print(lst1)
print(lst1[-1], lst1[-2], lst1[-3])