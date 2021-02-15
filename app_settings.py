import pygame.font


class Settings:
    """Класс для хранения настроек"""
    def __init__(self):
        # Параметры экрана
        self.screen_height = 700
        self.screen_width = 700
        self.bg_color = (150, 150, 230)

        # Параметры текста главного меню
        self.main_text_color = (255, 215, 0)
        self.main_text_font = pygame.font.SysFont('verdana', 60, bold=True)

        # Парметры текста экрана расчёта ИМТ
        self.bmi_header_text_color = (255, 215, 0)
        self.bmi_header_text_font = pygame.font.SysFont('verdana', 50, bold=True)
        self.bmi_common_text_color = (0, 0, 139)
        self.bmi_common_text_font = pygame.font.SysFont('verdana', 35, bold=True)
        self.bmi_result_text_color = (169, 32, 62)
        self.bmi_result_text_font = pygame.font.SysFont('verdana', 35, bold=True)
        self.bmi_very_low_color = (148, 0, 211)
        self.bmi_low_color = (128, 0, 255)
        self.bmi_optimal_color = (190, 245, 116)
        self.bmi_high_color = (150, 75, 0)
        self.bmi_very_high_color = (166, 13, 16)

        # Параметры текста экрана расчёта нормального веса
        self.cnw_header_text_color = (255, 215, 0)
        self.cnw_header_text_font = pygame.font.SysFont('verdana', 50, bold=True)
        self.cnw_common_text_color = (0, 0, 139)
        self.cnw_common_text_font = pygame.font.SysFont('verdana', 35, bold=True)
        self.cnw_result_text_color = (169, 32, 62)
        self.cnw_result_text_font = pygame.font.SysFont('verdana', 35, bold=True)
        self.cnw_number_text_color = (255, 215, 0)
        self.cnw_number_text_font = pygame.font.SysFont('verdana', 35, bold=True, italic=True)

        # Параметры текста экрана графиков
        self.gw_header_text_color = (255, 215, 0)
        self.gw_header_text_font = pygame.font.SysFont('verdana', 50, bold=True)
        self.graph_common_text_color = (0, 0, 139)
        self.graph_common_text_font = pygame.font.SysFont('verdana', 45, bold=True)
        self.graph_error_text_color = (169, 32, 62)
        self.graph_bmi_title = "Daily BMI's"
        self.graph_weight_title = "Daily Weights"

        # Параметры текста экрана ввода данных текущего дня
        self.today_header_text_color = (255, 215, 0)
        self.today_header_text_font = pygame.font.SysFont('verdana', 50, bold=True)
        self.today_date_text_color = (169, 32, 62)
        self.today_date_text_font = pygame.font.SysFont('verdana', 30, bold=True)
        self.today_common_text_color = (0, 0, 139)
        self.today_common_text_font = pygame.font.SysFont('verdana', 35, bold=True)
        self.today_save_text_font = pygame.font.SysFont('verdana', 40, bold=True)

        # Параметры значка автора
        self.author_font = pygame.font.SysFont('verdana', 15)
        self.author_color = (100, 100, 100)

        # Прочее
        self.back_button_color = (166, 13, 16)
        self.exit_button_color = (166, 13, 16)
        self.fps = 60
