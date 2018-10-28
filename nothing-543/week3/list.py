liststring=[]
liststring.append(input('give me a letter'))
i=0
while liststring[i]:
    liststring.append(input('give me a letter'))
    i+=1
if 'x' in liststring:
    print(1)
else:
    print(0)
