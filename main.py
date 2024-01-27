'''Напишіть функцію, що визначає кількість простих чисел у списку цілих.
Список передається як параметр. Отриманий результат повертається з функції.'''

def Func(x):
    res = len(x)
    for el in x:
        if el < 2:
            res -= 1
        else:
            for i in range(1, el):
                if el % i == 0 and i > 1:
                    res -= 1
                    break
    return res

print(Func([2, 3, 4, 5, 6, 11, -1]))