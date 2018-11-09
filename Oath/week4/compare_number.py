import random
import timeit


def buddle(array:list) -> list:
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j+1] > array[j]:
                array[j], array[j+1] = array[j+1], array[j]
    return array[:3]


def select(array:list) -> list:
    length = len(array)
    for i in range(length):
        max_index = i
        for j in range(i+1, length):
            if array[j] > array[max_index]:
                max_index = j
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
    return array[:3]


def dual_select(array:list) -> list:
    length = len(array)
    for i in range(length//2):
        max_index = i
        min_index = -i - 1
        for j in range(i+1, length-i):
            if array[j] > array[max_index]:
                max_index = j
            if array[-j-1] > array[min_index]:
                min_index = -j -1
        if array[min_index] == array[max_index]:
            break
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            if i == min_index or i == length + min_index:
                min_index = max_index
        if -i-1 != min_index and array[-i-1] != array[min_index]:
            array[-i-1], array[min_index] = array[min_index], array[-i-1]
    return array[:3]


def insert_sort(array:list) -> list:
    length = len(lst)
    array = [0] + array
    for i in range(2, length+1):
        array[0] = array[i]
        j = i - 1
        if array[j] > array[0]:
            while array[j] > array[0]:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = array[0]
    return array[:-4:-1]


def heap_sort(array):
    def heap_adjust(n, i, array:list):
        while 2 * i <= n:
            lchild = 2 * i
            max_index = lchild
            if n > lchild and array[lchild+1] > array[max_index]:
                max_index = lchild + 1
            if array[max_index] > array[i]:
                array[max_index], array[i] = array[i], array[max_index]
                i = max_index
            else:
                break

    def max_heap(n, array:list):
        for i in range(n//2, 0, -1):
            heap_adjust(n, i, array)
        return lst

    array.insert(0, 0)
    length = len(array)-1
    max_heap(length, array)
    while length > 1:
        array[1], array[length] = array[length], array[1]
        length -= 1
        heap_adjust(length, 1, array)
    return array[:-4:-1]


lst = [random.randint(1, 99) for _ in range(20)]

print(buddle(lst))
print(timeit.timeit('buddle(lst)', number=100000, globals=globals()))
print('=' * 20)

print(select(lst))
print(timeit.timeit('select(lst)', number=100000, globals=globals()))
print('=' * 20)

print(dual_select(lst))
print(timeit.timeit('dual_select(lst)', number=100000, globals=globals()))
print('=' * 20)

print(insert_sort(lst))
print(timeit.timeit('insert_sort(lst)', number=100000, globals=globals()))
print('=' * 20)

print(heap_sort(lst))
print('=' * 20)