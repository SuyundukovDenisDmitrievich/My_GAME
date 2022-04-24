import pygame, controls


# Создаём отдельный класс для пушки
class Gun:

    def __init__(self, screen):
        """ Инициализация пушки """
        # Получаем экран
        self.screen = screen
        # Загружаем саму картинку пушки
        self.image = pygame.image.load("images/gun_img.png")
        # распологаем нашу пушку на фоновом экране (перед фоновым экраном )
        # эта строка означает расположение нашей картинки как прямоугольник
        self.rect = self.image.get_rect()
        # Получаем графический объект экрана
        self.screen_rect = screen.get_rect()
        # Расположение пушки на экране по координатам
        # Центр экрана расположение по горезонту
        self.rect.centerx = self.screen_rect.centerx
        # для приёма вещественных (дробных) чисел
        self.center = float(self.rect.centerx)
        # Назначение нижней точки на экране расположения нашей пушки
        self.rect.bottom = self.screen_rect.bottom
        # для перемещения с зажатой клавишой
        self.mright = False
        self.mleft = False

    # Функция выводящая пушку на экран
    def output(self):
        """ Отрисовка пушки на экране """
        # Отрисовываем пушку на экране и задаем её как прямоугольник
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """ Функция запоминает позицию пушки и обновляет её"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5
        # Подключение этого атрибута
        self.rect.centerx = self.center
