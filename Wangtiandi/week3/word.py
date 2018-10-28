with open('python.txt') as f_obj:
	s = f_obj.read()
l = s.replace(',', ' ').replace('.', ' ').split()
print('This text has {} words.'.format(len(l)))
