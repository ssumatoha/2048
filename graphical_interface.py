import pygame
from logic import *

BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS+1) * MARGIN
HEIGHT = WIDTH + 110
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def search_num(x):  # Поиск одинаковых чисел рядом
    output = False
    for i in range(4):
        for j in range(3):
            if x[i][j] == x[i][j + 1]:
                output = True
                return output
            else:
                output = False
    for i in range(3):
        for j in range(4):
            if x[i][j] == x[i + 1][j]:
                output = True
                return output
    return output


def run():  # Функция запуска игры с графическим интерфейсом
    mas = [  # массив с игровым полем
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    mas_coord = [  # массив с координатами клеток
        [[65, 68], [186, 68], [307, 68], [428, 68]],
        [[65, 187], [186, 187], [307, 187], [428, 187]],
        [[65, 306], [186, 306], [307, 306], [428, 306]],
        [[65, 425], [186, 425], [307, 425], [428, 425]],
    ]

    def draw(scr):  # функция отрисовки чисел
        for i in range(4):
            for j in range(4):
                number = mas[i][j]
                if number == 0:
                    number = ' '
                fontObj = pygame.font.Font('freesansbold.ttf', 50)
                textSurfaceObj = fontObj.render(f'{number}', True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (mas_coord[i][j][0], mas_coord[i][j][1])
                scr.blit(textSurfaceObj, textRectObj)

    pygame.init()  # инициализирую пайгейм
    screen = pygame.display.set_mode((WIDTH, HEIGHT - 110))  # Устанавливаю окно и указываю размер
    pygame.display.set_caption('2048')  # Указываю название игры
    bg_color = (187, 173, 160)  # переменная с кортежем - цвет фона
    screen.fill(bg_color)  # делаю заливку фона

    running = True
    while running:
        pygame.display.flip()  # "переворачиваю" экран
        for event in pygame.event.get():  # перебираю события
            if event.type == pygame.QUIT:  # если событие выход, то выхожу из цыкла
                running = False
            elif event.type == pygame.KEYDOWN:  # отрисовка пустых блоков
                for row in range(BLOCKS):
                    for column in range(BLOCKS):
                        w = column * SIZE_BLOCK + (column + 1) * MARGIN
                        h = row * SIZE_BLOCK + (row + 1) * MARGIN
                        pygame.draw.rect(screen, WHITE, (w, h, 110, 110))
                if event.key == pygame.K_UP:
                    mas = go_top(mas)
                    randomizing(mas)
                    draw(screen)
                elif event.key == pygame.K_DOWN:
                    mas = go_bot(mas)
                    randomizing(mas)
                    draw(screen)
                elif event.key == pygame.K_LEFT:
                    go_left(mas)
                    randomizing(mas)
                    draw(screen)
                elif event.key == pygame.K_RIGHT:
                    go_right(mas)
                    randomizing(mas)
                    draw(screen)
                if len(search_mas_zero(mas)) == 1 and search_num(mas) == False:  # проверка на поражение
                    print('вы проиграли')
                    fontObj = pygame.font.Font('freesansbold.ttf', 50)
                    textSurfaceObj = fontObj.render('ВЫ ПРОИГРАЛИ!!', True, BLACK, WHITE)
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (250, 250)
                    screen.blit(textSurfaceObj, textRectObj)
                if search2048(mas) == True:
                    print('вы победили')
                    fontObj = pygame.font.Font('freesansbold.ttf', 50)
                    textSurfaceObj = fontObj.render('ВЫ ПОБЕДИЛИ!!', True, BLACK, WHITE)
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (250, 250)
                    screen.blit(textSurfaceObj, textRectObj)


run()
