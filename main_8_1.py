def add_everything_up(a, b):
    return a + b

try:
    print(add_everything_up(123.456, 'строка'))
    #код ниже не будет выполняться
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
except TypeError as exc:
    print(f'Произошла ошибка: {exc}')
    print(f'Вы пытаетесь сложить два числа! Ладно, в этот раз сложим:')
    print(f'{str(4215) + " строка"}')
else:
    print('Эх, до меня дело не дойдёт :(')
finally:
    print('Так или иначе код выполнили!\n')

try:
    print(add_everything_up('яблоко', 4215))
except TypeError as exc:
    print(f'Произошла ошибка: {exc}')
    print('Вы пытаетесь сложить два числа! Ладно, в этот раз сложим:')
    print(f'{"яблоко " + str(4215)}')
else:
    print('Эх, до меня дело не дойдёт :(')
finally:
    print('Так или иначе код выполнили!\n')

try:
    print(add_everything_up(123.456, 7))
except TypeError as exc:
    print('Эх, теперь до меня дело не дойдёт >:(')
else:
    print('Ошибка не допущена!')
finally:
    print('Так или иначе код выполнили!')
