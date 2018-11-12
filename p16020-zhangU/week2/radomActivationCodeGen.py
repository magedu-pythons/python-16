import random
import string

stringCode = string.ascii_letters + string.digits
acCodeChooseList=[]
acCodeResults=[]

while(len(acCodeResults)<200):
    acCode = ''.join(random.sample(stringCode,5))
    if acCode in acCodeResults:
        continue;
    else:
        acCodeResults.append(acCode)
print(acCodeResults)  
