#shuffle a list
alist = [1,2,3,4,5]
print('{}\n{}{}'.format('Shuffle a list','The original list:',alist))
import random
random.shuffle(alist)
print('the shuffled list is:',alist)
print('~~~~~~~~~~~~~~~~~~~~')
#randomly show an item according to their stock
print('There are 10 pairs of socks, 20 pairs of shoes, 30 pairs of slippers, and 40 necklaces in this warehouse.'
      'Randomly show an item according to their stock.')
print(random.choices(['socks','shoes','slippers','necklaces'],[10,20,30,40],k=1))
