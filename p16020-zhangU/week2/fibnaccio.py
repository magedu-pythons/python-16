def print1():
    i=1
    while True:
        result = fab(i)
        if(result > 100):
            break
        print (result)
        i=i+1
def fab(n):
    if n==1 or n==2:
        return 1
    else:
        return fab(n-2)+fab(n-1)

def print2():
    fab1=1
    fab2=1
    while fab1<100:
        print (fab1)
        fabn=fab1+fab2
        fab1=fab2
        fab2=fabn
print("Fibonacci \r\n Result of Method one:\r")
print1()
print("Result of Method two:\r")
print2()