'''Напишіть функцію, що обчислює суму елементів списку цілих. Список передається як параметр.'''


def Sum(x, i=0, s=0):
    if i < len(x):
        return Sum(x, i+1, s+x[i])
    return s

a = [111, 222, 333]
print(Sum(a))