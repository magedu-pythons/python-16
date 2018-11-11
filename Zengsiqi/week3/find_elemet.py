from random import randint

lst=[]
for i in range(31):
    lst.append(randint(0,99))

key = 0


while key != "":
    key = input("Please input a integer(If Value is None will exit):")
    try:
        key = int(key)
    except ValueError:
        if key != "":
            print("Must input a integer")
    else:
        if lst.count(key):
            print(1)
        else:
            print(0)
print(lst)