
def gener_numlist(startnum,delta,num):
    for i in range(num+1):
        var = startnum+delta
        print('{}-{}'.format(startnum,var))
        startnum = var+1

gener_numlist(1,33,48)






