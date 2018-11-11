import inspect,functools

def check(fn):   #参数检查
	@functools.wraps(fn)
	def wrapper(*args,**kwargs):
		sig = inspect.signature(fn)
		params = sig.parameters
		values = list(params.values())
		for i,v in enumerate(args):
			if isinstance(v,values[i].annotation):
				pass
			else:
				print('wrong param')
				return
		for k,v in kwargs.items():
			if isinstance(v,params[k].annotation):
				pass
			else:
				print('wrong param')
				return
		x = fn(*args,**kwargs)
		return x
	return wrapper

#方法1
@check
def palindrome_num(n:int):
	n = str(n)
	if len(n) >= 2:
		if n[0] == n[-1]:
			n = n[1:-1]
			if n != '':
				return palindrome_num(int(n))
			else:
				print('It is a palindrome_num')
				return
		else:
			print('It is not a palindrome_num')
			return
	else:
		print('It is a palindrome_num')
		return


#方法2
@check
def palindrome_num(n:int):
    leng = len(str(n))
    mi = 10**(leng-1)
    if n > 9:
        i,j = (n//mi, n%10)
        if i == j:
            n = (n-i*mi)//10
            return palindrome_num(n)
        else:
            print('It is not a palindrome_num')
            return
    else:
        print('It is a palindrome_num')
        return

palindrome_num(12321)