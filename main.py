import pygame
import random


def run():
    pygame.init()  # инициализирую пайгейм
    screen = pygame.display.set_mode((1200, 800))  # Устанавливаю окно и указываю размер
    pygame.display.set_caption('2048')  # Указываю название игры
    bg_color = (187, 173, 160)  # переменная с кортежем - цвет фона

    running = True
    while running:
        for event in pygame.event.get():  # перебираю события
            if event.type == pygame.QUIT:  # если событие выход, то выхожу из цыкла
                running = False

        screen.fill(bg_color)  # делаю заливку фона
        pygame.display.flip()  # "переворачиваю" экран

run()
