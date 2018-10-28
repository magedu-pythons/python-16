# 使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import string
import random

chars = string.ascii_letters + string.digits
lst = []
code_number = 6
while len(lst) < 200:
    pre_code = random.sample(chars, code_number)
    activation_code = ''.join(pre_code)
    if activation_code not in lst:
        lst.append(activation_code)
print(lst)



"""
(0 + 0)
    
    完成的不错！
"""