string = "1,2,3"

def str_list(string:str):
    lst = []
    for c in string:
        if c not in ", ":
            lst.append(c)
    return lst

print(str_list(string))

