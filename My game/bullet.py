import pygame



# клас дял пуль на основе класса из библиотеки pygame
class Bullet(pygame.sprite.Sprite):


    def __init__(self, screen, gun):
        """Создаёт пулю в текущей позиции пушки"""
        # берём __init__ что у нас есть в класе sprite и применяем к нашему классу
        super(Bullet, self).__init__()
        # подзагружвем экран
        self.screen = screen
        # создаём позицию пули и саму пулю
        self.rect = pygame.Rect(0, 0, 2, 12)
        # цвет пули
        self.color = 0, 0, 0
        # скорость пули
        self.speed = 1.5
        # место появления пули (из дула) в центре нашей пушки
        self.rect.centerx = gun.rect.centerx
        # появление с верху где у нас конец дула пушки
        self.rect.top = gun.rect.top
        # координата перемещения пульки в дробных числах для плавного перемещения
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули вверх"""
        # перемещение нашей пули по оси y
        self.y -= self.speed
        #обновление позиции пули
        self.rect.y = self.y

    def draw_bullet(self):
        '''Рисуем пулю на экране'''
        pygame.draw.rect(self.screen, self.color, self.rect)


