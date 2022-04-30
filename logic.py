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


def randomizing(x):
    return random.choice(search_mas(x)), random.choice([2, 4])


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


print(randomizing(mas))
# print(*search_mas(mas))
# prnt(mas)
