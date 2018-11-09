#first

i=0
while hib(i)<100:
    print(hib(i))
    i+=1
def hib(i):
    if i<=0:
        return 1
    elif i==2:
        return 2
    else 
        return hib(i-1)+hib(i+1)


#second
m=[1,1]
i=2
while m[i-1]+m[i-2]<100:
    m.append(m[i-1]+m[i-2])
    i+=1
print(m)




"""
(0 + 0)
    
    第一个注意检查
"""