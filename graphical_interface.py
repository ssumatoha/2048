import pygame
from logic import *

BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS+1) * MARGIN
HEIGHT = WIDTH + 110
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

mas_coord = [
    [[65, 68], [186, 68], [307, 68], [428, 68]],
    [[65, 187], [186, 187], [307, 187], [428, 187]],
    [[65, 306], [186, 306], [307, 306], [428, 306]],
    [[65, 425], [186, 425], [307, 425], [428, 425]],
]


def draw(scr):
    for i in range(4):
        for j in range(4):
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            textSurfaceObj = fontObj.render(f'{mas[i][j]}', True, BLACK, WHITE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (mas_coord[i][j][0], mas_coord[i][j][1])
            scr.blit(textSurfaceObj, textRectObj)


def run(m):
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
                randomizing(m)
                draw(screen)
                if event.key == pygame.K_UP:
                    m = go_top(m)
                    draw(screen)


run(mas)
