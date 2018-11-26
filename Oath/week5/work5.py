# 打乱一个排好序的list对象alist
import random

def shuffle_lst(lst:list) -> list:
	random.shuffle(lst)
	return lst
array=[1, 2, 3, 4, 5]
print(shuffle_lst(array))

# 随机返回一种商品
def random_products(store:dict, item=[]):
	if not item:
		for k, v in store.items():
			item += [k] * v
	goods = random.choice(item)
	item.remove(goods)
	store[goods] -= 1
	if not store[goods]:
		store.pop(goods)
	return goods
store={'socks':10, 'shoe':20, 'slipper':30, 'necklace':40}
print(random_products(store))


"""
(0 + 0)

	2、函数形式参数不要用 list
"""