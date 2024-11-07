def add_everything_up(a, b):
    try:
        a + b
    except TypeError as exc:
        print(f'Произошла ошибка: {exc}')
        print('Вы пытаетесь сложить что-то отличное от чисел! Ладно, в этот раз сложим..')
        return str(a) + str(b)
    else:
        print('Ошибка не допущена!')
        return a + b
    finally:
        print('Так или иначе код выполнили!')
