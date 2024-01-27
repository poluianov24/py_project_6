'''Напишіть функцію, що видаляє зі списку цілих деяке задане число.
З функції потрібно повернути кількість видалених елементів.'''

def Func(x, y):
    res = 0
    for i in x:
        if i == y:
            res += 1
            x.remove(y)
            for a in x:
                if a == y:
                    res += 1
                    x.remove(y)
    return res

print(Func([11, 2, 2, 2, 5, 2, 3, 4, 6, 2, 5], 2))