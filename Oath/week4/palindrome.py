def is_palindrome(num:int):
    num = str(num)
    for i in range(len(num)//2):
        if num[i] != num[-i-1]:
            return "{} isn't palindrome number".format(num)
    else:
        return "{} is palindrome number".format(num)


def palindrome(num:int):
    num = str(num)
    if num[::-1] == num:
        return "{} is palindrome number".format(num)
    else:
        return "{} isn't palindrome number".format(num)


while True:
    num = int(input('input a number >>>'))
    if num < 0:
        print("{} isn't palindrome number".format(num))
        break
    print(is_palindrome(num))
    print('='*20)
    print(palindrome(num))