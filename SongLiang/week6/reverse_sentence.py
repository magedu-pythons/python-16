sen = 'Sometimes,the life is not so easy,you need to keep hope and carry on.'
chars = ', .'
def make_words(sen):
	start = 0
	lst = []
	for i,v in enumerate(sen):
		if v in chars:
			if start == i:
				start += 1
				continue
			lst.append(sen[start:i])
			start = i + 1
	if start < len(sen):
		lst.append(sen[start:])
	return lst

def reverse_word(sen):
	lst = make_words(sen)
	return [lst[x] for x in range(len(lst)-1, -1, -1)]


	
print(reverse_word(sen))