# 使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于 5 以上
import random

letters = []
random_numbers = []

# 随机数取值范围列表
for i in range(ord('a'), ord('z')):
    letters.append(chr(i))
letters.extend(range(10))

while len(random_numbers) < 200:
    letter = ''
    for s in random.sample(letters, 6):
        letter += str(s)
    
    random_numbers.append(letter.upper())
    # 删除重复随机数
    for rnd in random_numbers:
        while random_numbers.count(rnd) >= 2:
            random_numbers.remove(rnd)
else:
    print(random_numbers)
