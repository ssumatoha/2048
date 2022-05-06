from logic import *


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


def game(x):
    while True:
        if len(search_mas_zero(x)) == 1:
            print('вы проиграли')
            break
        elif search2048(x) == False:
            print('вы победили')
            break
        randomizing(x)
        prnt(x)
        a = input('Введите команду: ')
        if a == 'w':
            x = go_top(x)
            prnt(x)
        elif a == 's':
            x = go_bot(x)
            prnt(x)
        elif a == 'a':
            go_left(x)
            prnt(x)
        elif a == 'd':
            go_right(x)
            prnt(x)
        elif a == 'q':
            print('выход')
            break