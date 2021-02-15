import sys

import pygame


class EntryPole:
    """Класс поля ввода"""

    def __init__(self, center_x, center_y, width=140, height=40, font_size=32):
        """Инициализирует атрибуты поля ввода"""
        self.font = pygame.font.SysFont('verdana', font_size)
        self.width = width
        self.height = height
        self.input_box_rect = pygame.Rect(center_x - self.width // 2, center_y - self.height // 2, self.width,
                                          self.height)
        self.active_color = (243, 218, 11)
        self.passive_color = (0, 0, 0)
        self.color = self.passive_color
        self.active = False
        self.center_x = center_x
        self.center_y = center_y

    def check_events(self, event, name, maxlen=6):
        """Проверка нажатий"""
        name = str(name)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box_rect.collidepoint(event.pos[0], event.pos[1]):
                self.active = not self.active
            else:
                self.active = False
            if self.active:
                self.color = self.active_color
            else:
                self.color = self.passive_color
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_RETURN:
                self.active = False
                self.color = self.passive_color
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) <= maxlen - 1:
                    if (event.unicode in '1234567890') or (event.unicode == '.' and '.' not in name):
                        name += event.unicode
        return name

    def update_pole(self, screen, settings, name, color=(169, 32, 62)):
        """Обновление поля ввода"""
        screen.fill(settings.bg_color, self.input_box_rect)
        name_image = self.font.render(str(name), 1, color)
        name_image_rect = name_image.get_rect()
        name_image_rect.center = (self.center_x, self.center_y)
        self.input_box_rect.center = (self.center_x, self.center_y)
        screen.blit(name_image, name_image_rect)
        pygame.draw.rect(screen, self.color, self.input_box_rect, 2)
        pygame.display.flip()
