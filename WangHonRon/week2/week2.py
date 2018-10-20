#作业2、打印出100以内的斐波那契数列，使用2种方法实现
#100以内斐波那契数列
n=100
#方法一： 
f0 = 1
f1 = 1
print(f0,f1,sep='\n')
for i in range(1,n):
	fn=f0+f1
	if fn > 100: break
	print(fn)
	f0 = f1
	f1 = fn
#方法二： 
f2 = 1
f3 = 1
print(f2,f3,sep='\n')
while True:
    fm = f2 + f3
    if fm > n: break
	print(fm)
    f2 = f3
    f3 = fm   
	
	
#作业3、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
