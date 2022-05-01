import random


def rotate_matrix(x):  # функция поворота матрицы
    return [[x[j][i] for j in range(len(x))] for i in range(len(x[0])-1, -1, -1)]


def prnt(x):  # функция красивого вывода
    print('-' * 10)
    for i in x:
        print(*i)
    print('-' * 10)


def search_mas_zero(x):  # функция поиска нулевых значений
    list_zero = []
    for i in range(4):
        for j in range(4):
            if x[i][j] == 0:
                list_zero.append([i, j])
    return list_zero


def randomizing(x):  # функция рандомного заполнения нулевых значений
    random_elem = random.choice(search_mas_zero(x))
    x[random_elem[0]][random_elem[1]] = random.choice([2, 4])


def go_left(x):  # функция-свайп влево
    for i in x:
        for j in range(3):
            if i[j] == 0 and i[j + 1] != 0:
                i[j] = i[j + 1]
                i[j + 1] = 0
                go_left(x)


def go_right(x):  # функция-свайп вправо
    [i.reverse() for i in x]
    go_left(x)
    [i.reverse() for i in x]


def go_top(x):  # функция-свайп вверх
    x = rotate_matrix(x)
    go_left(x)
    for i in range(3):
        x = rotate_matrix(x)
    return x


def go_bot(x):  # функция-свайп вниз
    for i in range(3):
        x = rotate_matrix(x)
    go_left(x)
    x = rotate_matrix(x)
    return x


mas = [
    [3, 0, 2, 0],
    [0, 4, 0, 0],
    [0, 0, 5, 0],
    [0, 0, 0, 0],
]

#prnt(mas)
randomizing(mas)
prnt(mas)
mas = go_bot(mas)
#go_right(mas)
prnt(mas)
# print(*search_mas(mas))
# prnt(mas)
