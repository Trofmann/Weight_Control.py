import pygame


def draw_author(screen, settings):
    """Отрисовка автора"""
    draw_text(screen, "© 2020 Evgeniy Trofimov", settings.screen_width // 2, settings.screen_height - 10,
              settings.author_color, settings.author_font, )


def draw_bmi_window(screen, settings, data, back_button, calculate_button, bmi_height_pole, bmi_weight_pole):
    """Отрисовка экрана расчёта ИМТ"""
    screen.fill(settings.bg_color)
    draw_author(screen, settings)
    draw_text(screen, "Calculate", settings.screen_width // 2, 40, settings.bmi_header_text_color,
              settings.bmi_header_text_font)
    draw_text(screen, "Body Mass Index", settings.screen_width // 2, 90, settings.bmi_header_text_color,
              settings.bmi_header_text_font)
    draw_text(screen, "Enter your weight: ", 230, 200, settings.bmi_common_text_color, settings.bmi_common_text_font)
    draw_text(screen, "kg", 610, 200, settings.bmi_common_text_color, settings.bmi_common_text_font)
    draw_text(screen, "Enter your height: ", 227, 300, settings.bmi_common_text_color, settings.bmi_common_text_font)
    draw_text(screen, "cm", 610, 300, settings.bmi_common_text_color, settings.bmi_common_text_font)
    back_button.draw_button()
    calculate_button.draw_button()
    bmi_height_pole.update_pole(screen, settings, data.bmi_height)
    bmi_weight_pole.update_pole(screen, settings, data.bmi_weight)
    pygame.display.flip()


def draw_bmi_result(screen, settings, color, text1, text2):
    """Отрисовка результата расчёта ИМТ"""
    pygame.draw.rect(screen, settings.bg_color, (0, 350, 700, 200))
    draw_text(screen, text1, settings.screen_width // 2, 400, color, settings.bmi_common_text_font)
    draw_text(screen, text2, settings.screen_width // 2, 450, color, settings.bmi_common_text_font)
    pygame.display.flip()


def draw_cnw_window(screen, settings, data, back_button, calculate_button, cnw_height_pole):
    """Отрисовка экрана расчёта нормального веса"""
    screen.fill(settings.bg_color)
    draw_author(screen, settings)
    draw_text(screen, "Calculate", settings.screen_width // 2, 40, settings.cnw_header_text_color,
              settings.cnw_header_text_font)
    draw_text(screen, "Optimal Weight", settings.screen_width // 2, 90, settings.cnw_header_text_color,
              settings.cnw_header_text_font)
    draw_text(screen, "Enter your height: ", 227, 200, settings.cnw_common_text_color, settings.cnw_common_text_font)
    draw_text(screen, "cm", 630, 200, settings.cnw_common_text_color, settings.cnw_common_text_font)
    cnw_height_pole.update_pole(screen, settings, data.cnw_height)
    back_button.draw_button()
    calculate_button.draw_button()
    pygame.display.flip()


def draw_cnw_result(screen, settings, data):
    """Отрисовка оптимального веса"""
    pygame.draw.rect(screen, settings.bg_color, (0, 350, 700, 250))
    draw_text(screen, "Your optimal weight: ", 247, 350, settings.cnw_result_text_color,
              settings.cnw_result_text_font)
    draw_text(screen, "From ", 100, 430, settings.cnw_result_text_color, settings.cnw_result_text_font)
    draw_text(screen, str(data.cnw_min_weight), 213, 430, settings.cnw_number_text_color, settings.cnw_number_text_font)
    draw_text(screen, "to ", 303, 430, settings.cnw_result_text_color, settings.cnw_result_text_font)
    draw_text(screen, str(data.cnw_max_weight), 380, 430, settings.cnw_number_text_color, settings.cnw_number_text_font)
    draw_text(screen, "kilograms ", 550, 430, settings.cnw_result_text_color,
              settings.cnw_result_text_font)
    pygame.display.flip()


def draw_graphs_window(screen, settings, back_button, show_bmi_button, show_weight_button):
    """Отрисовка экрана графиков"""
    screen.fill(settings.bg_color)
    draw_author(screen, settings)
    draw_text(screen, "Graphs", settings.screen_width // 2, 40, settings.gw_header_text_color,
              settings.gw_header_text_font)
    draw_text(screen, "Body Mass Index graph:", settings.screen_width // 2, 200, settings.graph_common_text_color,
              settings.graph_common_text_font)
    draw_text(screen, "Weight graph:", settings.screen_width // 2, 400, settings.graph_common_text_color,
              settings.graph_common_text_font)
    back_button.draw_button()
    show_bmi_button.draw_button()
    show_weight_button.draw_button()
    pygame.display.flip()


def draw_main_menu(screen, settings, calculate_bmi_button, calculate_normal_weight_button, graphs_button,
                   today_button, exit_button):
    """Отрисока главного меню"""
    screen.fill(settings.bg_color)
    draw_author(screen, settings)
    draw_text(screen, "Weight control", settings.screen_width // 2, 40, settings.main_text_color,
              settings.main_text_font)
    calculate_bmi_button.draw_button()
    exit_button.draw_button()
    calculate_normal_weight_button.draw_button()
    graphs_button.draw_button()
    today_button.draw_button()
    pygame.display.flip()


def draw_text(screen, text, center_x, center_y, color, font):
    """Отрисовка текста"""
    text_image = font.render(str(text), 1, color)
    text_rect = text_image.get_rect()
    text_rect.center = (center_x, center_y)
    screen.blit(text_image, text_rect)
    pygame.display.flip()


def draw_today_window(screen, settings, data, back_button, save_button, reset_button, today_weight_pole,
                      today_height_pole):
    """Отрисовка экрана ввода данных текущего дня"""
    screen.fill(settings.bg_color)
    draw_author(screen, settings)
    draw_text(screen, "Today's values", settings.screen_width // 2, 40, settings.today_header_text_color,
              settings.today_header_text_font)
    draw_text(screen, data.today_nice_date, settings.screen_width // 2, 90, settings.today_date_text_color,
              settings.today_date_text_font)
    draw_text(screen, "Enter today's weight:", 230, 250, settings.today_common_text_color,
              settings.today_common_text_font)
    draw_text(screen, "Enter today's height:", 230, 350, settings.today_common_text_color,
              settings.today_common_text_font)
    draw_text(screen, "kg", 640, 250, settings.bmi_common_text_color, settings.bmi_common_text_font)
    draw_text(screen, "cm", 640, 350, settings.bmi_common_text_color, settings.bmi_common_text_font)
    today_weight_pole.update_pole(screen, settings, data.today_weight)
    today_height_pole.update_pole(screen, settings, data.today_height)
    back_button.draw_button()
    save_button.draw_button()
    reset_button.draw_button()
    pygame.display.flip()
