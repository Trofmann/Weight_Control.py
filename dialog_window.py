import sys

import pygame

from button import Button


class DialogWindow:
    """Класс диалогового окна"""

    def __init__(self, screen, center_x, center_y, width=400, height=150):
        """Инициализирует атрибуты """
        # Параметры диалогового окна
        self.screen = screen
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.bg_color = (200, 200, 200)
        self.frame_color = (243, 218, 11)
        self.text_color = (90, 90, 90)
        self.font_size = 30
        self.font = pygame.font.SysFont('verdana', self.font_size)

        # Создание кнопок "Yes" и "No"
        self.yes_button = Button(self.screen, center_x - 100, center_y + 50, "Yes", width=100, height=40)
        self.no_button = Button(self.screen, center_x + 100, center_y + 50, "No", width=100, button_color=(166, 13, 16),
                                height=40)

        # Построение прямоугольника диалогового окна
        self.window_rect = pygame.Rect(0, 0, self.width, self.height)
        self.window_rect.center = (self.center_x, self.center_y)

        # Создание текста диалогового окна
        self.prep_text()

    def draw_window(self):
        """Рисует диалоговое окна"""
        self.screen.fill(self.bg_color, self.window_rect)
        self.screen.blit(self.text1_image, self.text1_image_rect)
        self.screen.blit(self.text2_image, self.text2_image_rect)
        pygame.draw.rect(self.screen, self.frame_color, self.window_rect, 4)
        self.no_button.draw_button()
        self.yes_button.draw_button()
        pygame.display.flip()

    def prep_text(self):
        """Подгтовка текста к выводу"""
        self.text1_image = self.font.render("Are you sure want", 1, self.text_color, self.bg_color)
        self.text1_image_rect = self.text1_image.get_rect()
        self.text1_image_rect.center = (self.window_rect.centerx, self.window_rect.centery - 50)
        self.text2_image = self.font.render("to reset data?", 1, self.text_color, self.bg_color)
        self.text2_image_rect = self.text2_image.get_rect()
        self.text2_image_rect.center = self.window_rect.center

    def check_buttons(self, mouse_x, mouse_y):
        """Проверка нажатий на кнопки"""
        no_button_clicked = self.no_button.check_clicked(mouse_x, mouse_y)
        yes_button_clicked = self.yes_button.check_clicked(mouse_x, mouse_y)
        return yes_button_clicked, no_button_clicked

    def check_events(self):
        """Проверка нажатий диалогового окна"""
        yes_button_clicked, no_button_clicked = False, False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                yes_button_clicked, no_button_clicked = self.check_buttons(mouse_x, mouse_y)
        return yes_button_clicked, no_button_clicked
