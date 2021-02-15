import pygame

import functions as func
from app_data import Data
from app_settings import Settings
from button import Button
from dialog_window import DialogWindow
from entry_pole import EntryPole


def run_app():
    """Инициализация приложения"""
    # Инициализация экрана, настроек, данных
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Weight control by Evgeniy Trofimov")
    func.loading_window(screen, settings)
    data = Data()

    # Создание кнопок
    calculate_button = Button(screen, settings.screen_width - 150, settings.screen_height - 50, "Calculate", width=200)
    calculate_bmi_button = Button(screen, settings.screen_width // 2, settings.screen_height // 4, "Calculate BMI")
    exit_button = Button(screen, settings.screen_width // 2, settings.screen_height - settings.screen_height // 4,
                         "Exit", button_color=settings.exit_button_color)
    calculate_normal_weight_button = Button(screen, settings.screen_width // 2, settings.screen_height // 4 + 75,
                                            "Calculate optimal weight")
    graphs_button = Button(screen, settings.screen_width // 2, settings.screen_height // 4 + 225, "Graphs")
    back_button = Button(screen, settings.screen_width // 2, settings.screen_height - 50, "Back", width=100,
                         button_color=settings.back_button_color)
    today_button = Button(screen, settings.screen_width // 2, settings.screen_height // 4 + 150, "Enter today's data")
    show_bmi_button = Button(screen, settings.screen_width // 2, 300, "Show", width=200)
    show_weight_button = Button(screen, settings.screen_width // 2, 500, "Show", width=200)
    save_button = Button(screen, settings.screen_width - 150, settings.screen_height - 50, "Save", width=200)
    reset_button = Button(screen, 150, settings.screen_height - 50, "Reset data", width=200)

    # Создание полей ввода
    cnw_height_pole = EntryPole(500, 200)
    bmi_height_pole = EntryPole(500, 300)
    bmi_weight_pole = EntryPole(500, 200)
    today_weight_pole = EntryPole(530, 250)
    today_height_pole = EntryPole(530, 350)

    # Создание диалогового окна
    dialog_window = DialogWindow(screen, settings.screen_width // 2, settings.screen_height // 2)

    # Главное меню
    func.main_menu(screen, settings, data, calculate_bmi_button, calculate_normal_weight_button, graphs_button,
                   today_button, exit_button, back_button, calculate_button, show_bmi_button, show_weight_button,
                   save_button, reset_button, cnw_height_pole, bmi_height_pole, bmi_weight_pole, today_weight_pole,
                   today_height_pole, dialog_window)


run_app()
