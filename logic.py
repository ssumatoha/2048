import random


def prnt(x):
    for i in x:
        print(*i)


def search_mas(x):
    list_zero = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                list_zero.append([i, j])
    return list_zero


def randomizing():
    pass


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


print(*search_mas(mas))
# prnt(mas)
