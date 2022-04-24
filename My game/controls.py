import pygame
import sys
from bullet import Bullet



def events(screen, gun, bullets):
    """
    Обработка событий
    gun : объект который будем передвигать
    """
    # обрабатывает полученные команды
    for event in pygame.event.get():
        # условие закрытия окна программы
        if event.type == pygame.QUIT:
            # Функция закрытия
            sys.exit()
        # Условие: если клавиша нажата
        elif event.type == pygame.KEYDOWN:
            # проверка какая именно нажата клавиша
            if event.key == pygame.K_RIGHT:
                # передвежение от центра в право.
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                # передвежение от центра в  лево).
                gun.mleft = True
                # Нажата кнопка Пробел
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                # добавляем в список нашу пульку
                bullets.add(new_bullet)
        # если клавиша отжата проверка
        elif event.type == pygame.KEYUP:
            # Если отжата клавиша в право
            if event.key == pygame.K_RIGHT:
                # Не двигаеться пушка
                gun.mright = False
                # Если отжата клавиша в лево
            elif event.key == pygame.K_LEFT:
                # Не двигаеться пушка
                gun.mleft = False


def update (bg_color, screen, gun, bullets):
    """Функция обновления экрана"""
    # присвоение цвета фона окна игры
    screen.fill(bg_color)
    # отображаем пульки
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # отрисовываем пушку на экране
    gun.output()
    # последний экран
    pygame.display.flip()
def update_bullets(bullets):
    """Обновляет позиции пуль"""
    # отрисовка и помещение на экран наших пуль
    bullets.update()
    # для уменьшения занимаемой памяти и удаления пуля во избежании её полята до бесконечности
    for bullet in bullets.copy():
        # Проверяем положение низа пули и если оно уходит за экран мы его удаляем
        if bullet.rect.bottom <= 0:
            # Удаляем пулю
            bullets.remove(bullet)


