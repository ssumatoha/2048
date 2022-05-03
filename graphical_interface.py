import pygame

BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS+1) * MARGIN
HEIGHT = WIDTH + 110
WHITE = (255, 255, 255)


def run():
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


run()
