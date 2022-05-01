import random


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


def go_right(x):
    for i in x:
        i.reverse()
        for j in range(3):
            if i[j] == 0 and i[j + 1] != 0:
                i[j] = i[j + 1]
                i[j + 1] = 0
        i.reverse()


mas = [
    [32, 4, 16, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

#prnt(mas)
randomizing(mas)
prnt(mas)
go_right(mas)
prnt(mas)
# print(*search_mas(mas))
# prnt(mas)
