from logic import *

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

while True:
    if len(search_mas_zero(mas)) == 1:
        print('вы проиграли')
        break
    elif search2048(mas) == False:
        print('вы победили')
        break
    randomizing(mas)
    prnt(mas)
    a = input('Введите команду: ')
    if a == 'w':
        mas = go_top(mas)
        prnt(mas)
    elif a == 's':
        mas = go_bot(mas)
        prnt(mas)
    elif a == 'a':
        go_left(mas)
        prnt(mas)
    elif a == 'd':
        go_right(mas)
        prnt(mas)
    elif a == 'q':
        print('выход')
        break
