import re
 
file_name = input('give me a filename')

words_dict = {}
lines_list = []
 
with open(file_name, 'r') as word:
    for line in word:
        match = re.findall(r'[^a-zA-Z0-9]+', line)
        for i in match:
            line = line.replace(i, ' ')
        lines_list = line.split()
        for i in lines_list:
            if i not in words_dict:
                words_dict[i] = 1
            else:
                words_dict[i] = words_dict[i] + 1 
for k,v in words_dict.items():
    print(k,v)



"""
(0 + 0)

    做的不错，建议使用函数封装
"""