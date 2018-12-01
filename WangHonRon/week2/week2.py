# 1.搭建pytenv环境，理解local/global/shell方式区别，并安装运行jupyter
#安装pyenv
#curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
#cat ~/.bash_profile
#export PATH='/home/hans/.pyenv/bin:$PATH"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"

# 2.求100以内斐波那契数列，用两种方式实现
# Fibonacci in 100，method one
print('*'*10,'Fibonacci one','*'*10)
a = 1
b = 1
n = 0
lst = [a,b]
for i in range(100):
    n = a + b
    if n > 100: break
    lst.append(n)
    a = b
    b = n
print(lst)

# Fibonacci in 100,method two
print('*'*10,'Fibonacci two','*'*10)
a = 1
b = 1
c = 0
print(a,b,sep = '\n')
while True:
    c = a + b
    if c > 100: break
    print(c)
    a = b
    b = c

# 3.随机生成200个无重复激活码，字符串长度大于5以上
import random
import string 
print('*'*10,'随机生成200个无重复激活码，长度为9','*'*10)
strsource = string.ascii_letters + string.digits
actcodelenth = 9
actlist = []
for i in range(200):
    #构建指定长度激活码
    codestr = ''.join(random.sample(strsource,k=actcodelenth))
    if codestr not in actlist:
        #添加到激活码库
        actlist.append(codestr)
print(actlist)



"""
(0 + 0)

    没有导入相关模块，程序运行测试成功后再进行提交
"""