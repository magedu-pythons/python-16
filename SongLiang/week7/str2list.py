#方法1
n = '1,2,3'
lst = n.split(',')
print(lst)


#方法2
import re

n = '1,2,3'
regex = re.compile('\d')
result = regex.findall(n)
print(result)