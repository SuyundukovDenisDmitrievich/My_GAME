import pygame
import controls
import sys
from gun import Gun
from pygame.sprite import Group




def run():
    # инициализация
    pygame.init()
    # создание дисплея и его размер в пикселях в кортеже
    screen = pygame.display.set_mode((1200, 800))
    # название игры
    pygame.display.set_caption("МТ-12 Рапира против ХОХЛОВ")
    # цвет фона экрана игры
    bg_color = (114, 134, 57)
    # импортируем и отрисовываем нашу пушку
    gun = Gun(screen)
    #создаём список для наших пуль
    bullets = Group()

    # Цикл в котором будут отслежоваться все действия игрока
    while True:
        # вызываем функцию ответственную за события
        controls.events(screen, gun, bullets)
        # Вызываем функцию ответсвенную за обновление позиции пушки
        gun.update_gun()
        # Обновление экрана
        controls.update(bg_color, screen, gun, bullets)
        # отрисовка и помещение на экран наших пуль
        controls.update_bullets(bullets)

run()