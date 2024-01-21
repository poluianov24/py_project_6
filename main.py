'''Напишіть функцію, що визначає кількість парних, непарних, додатних,
від'ємних елементів списку цілих. Список передається як параметр.'''


def Func(x):
    par = 0
    no_par = 0
    plus = 0
    minus = 0
    for i in x:
        if i % 2 == 0:
            par += 1
            if i < 0:
                minus +=1
            else:
                plus +=1
        else:
            no_par += 1
            if i < 0:
                minus +=1
            else:
                plus +=1
    print(f'Парних чисел: {par}')
    print(f'Непарних чисел: {no_par}')
    print(f'Додатніх чисел: {plus}')
    print(f'Відємних чисел: {minus}')

    return




if __name__ == '__main__':
    Func([1, 4, -3, 'f', 32])