import sys

import pygame

import drawer
import graphs


def bmi_window(screen, settings, data, back_button, calculate_button, bmi_height_pole, bmi_weight_pole):
    """Меню расчёта ИМТ"""
    drawer.draw_bmi_window(screen, settings, data, back_button, calculate_button, bmi_height_pole, bmi_weight_pole)
    back_button_clicked = False

    while not back_button_clicked:
        back_button_clicked, calculate_button_clicked, return_pressed = check_bmi_events(screen, settings, data,
                                                                                         back_button,
                                                                                         calculate_button,
                                                                                         bmi_height_pole,
                                                                                         bmi_weight_pole)
        # Расчёт ИМТ
        if calculate_button_clicked or return_pressed:
            data.bmi_bmi = calc_bmi(data.bmi_height, data.bmi_weight)
            color, result_text, phrase = determine_bmi_result(settings, data.bmi_bmi)
            drawer.draw_bmi_result(screen, settings, color, result_text, phrase)


def calc_bmi(height, weight):
    """Расчёт ИМТ"""
    temp_height = float(height) / 100
    temp_weight = float(weight)
    temp_bmi = round((temp_weight / (temp_height ** 2)), 2)
    return temp_bmi


def calc_normal_weight(height):
    """Расчёт оптимального веса"""
    height = float(height) / 100
    min_weight = round(18.5 * (height ** 2), 2)
    max_weight = round(25 * (height ** 2), 2)
    return min_weight, max_weight


def check_bmi_events(screen, settings, data, back_button, calculate_button, bmi_height_pole, bmi_weight_pole):
    """Проверка событий меню расчёта ИМТ"""
    back_button_clicked = False
    calculate_button_clicked = False
    return_pressed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Проврка нажатий на кнопки
                mouse_x, mouse_y = pygame.mouse.get_pos()
                back_button_clicked = back_button.check_clicked(mouse_x, mouse_y)
                calculate_button_clicked = calculate_button.check_clicked(mouse_x, mouse_y)

            # Ввод данных
            data.bmi_height = bmi_height_pole.check_events(event, data.bmi_height)
            if not bmi_height_pole.active:
                if data.bmi_height == '':
                    data.bmi_height = 170.0
                else:
                    if float(data.bmi_height) == 0:
                        data.bmi_height = 170.0
                    data.bmi_height = str(float(data.bmi_height))

            data.bmi_weight = bmi_weight_pole.check_events(event, data.bmi_weight)
            if not bmi_weight_pole.active:
                if data.bmi_weight == '':
                    data.bmi_weight = 60.0
                else:
                    data.bmi_weight = float(data.bmi_weight)

            bmi_height_pole.update_pole(screen, settings, data.bmi_height)
            bmi_weight_pole.update_pole(screen, settings, data.bmi_weight)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    return_pressed = True

    return back_button_clicked, calculate_button_clicked, return_pressed


def cnw_window(screen, settings, data, back_button, calculate_button, cnw_height_pole):
    """Меню расчёта оптимального веса"""
    drawer.draw_cnw_window(screen, settings, data, back_button, calculate_button, cnw_height_pole)
    back_button_clicked = False
    while not back_button_clicked:
        back_button_clicked, calculate_button_clicked, return_pressed = check_cnw_events(screen, settings, data,
                                                                                         back_button, calculate_button,
                                                                                         cnw_height_pole)
        if calculate_button_clicked or return_pressed:
            data.cnw_min_weight, data.cnw_max_weight = calc_normal_weight(data.cnw_height)
            drawer.draw_cnw_result(screen, settings, data)


def check_cnw_events(screen, settings, data, back_button, calculate_button, cnw_height_pole):
    """Проверка событий меню расчёта нормального веса"""

    back_button_clicked = False
    calculate_button_clicked = False
    return_pressed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Проверка нажатия на кнопки
                mouse_x, mouse_y = pygame.mouse.get_pos()
                back_button_clicked = back_button.check_clicked(mouse_x, mouse_y)
                calculate_button_clicked = calculate_button.check_clicked(mouse_x, mouse_y)

            # Проверка поля ввода
            data.cnw_height = cnw_height_pole.check_events(event, data.cnw_height)
            if not cnw_height_pole.active:
                if data.cnw_height == '':
                    data.cnw_height = 170.0
                else:
                    if float(data.cnw_height) == 0:
                        data.cnw_height = 170.0
                    data.cnw_height = float(data.cnw_height)
            cnw_height_pole.update_pole(screen, settings, data.cnw_height)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    return_pressed = True

    return back_button_clicked, calculate_button_clicked, return_pressed


def check_gw_events(back_button, show_bmi_button, show_weight_button):
    """Проверка событий меню графиков"""
    back_button_clicked = False
    show_bmi_button_clicked = False
    show_weight_button_clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка нажатий на кнопки
            mouse_x, mouse_y = pygame.mouse.get_pos()
            back_button_clicked = back_button.check_clicked(mouse_x, mouse_y)
            show_bmi_button_clicked = show_bmi_button.check_clicked(mouse_x, mouse_y)
            show_weight_button_clicked = show_weight_button.check_clicked(mouse_x, mouse_y)
    return back_button_clicked, show_bmi_button_clicked, show_weight_button_clicked


def check_main_menu_events(calculate_bmi_button, calculate_normal_weight_button, graphs_button, today_button,
                           exit_button):
    """Проверка событий в главном меню"""
    calculate_bmi_button_clicked = False
    calculate_normal_weight_button_clicked = False
    graphs_button_clicked = False
    today_button_clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Проверка нажатий на кнопки
            calculate_bmi_button_clicked = calculate_bmi_button.check_clicked(mouse_x, mouse_y)
            exit_button_clicked = exit_button.check_clicked(mouse_x, mouse_y)
            calculate_normal_weight_button_clicked = calculate_normal_weight_button.check_clicked(mouse_x, mouse_y)
            graphs_button_clicked = graphs_button.check_clicked(mouse_x, mouse_y)
            today_button_clicked = today_button.check_clicked(mouse_x, mouse_y)
            if exit_button_clicked:
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    return calculate_bmi_button_clicked, calculate_normal_weight_button_clicked, graphs_button_clicked, \
           today_button_clicked


def check_today_window_events(screen, settings, data, back_button, save_button, reset_button, today_weight_pole,
                              today_height_pole):
    """Проверка событий меню ввода данных текущего дня"""
    back_button_clicked = False
    save_button_clicked = False
    reset_button_clicked = False
    return_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Проверка нажатий на кнопки
                back_button_clicked = back_button.check_clicked(mouse_x, mouse_y)
                save_button_clicked = save_button.check_clicked(mouse_x, mouse_y)
                reset_button_clicked = reset_button.check_clicked(mouse_x, mouse_y)

            # Ввод данных
            data.today_weight = today_weight_pole.check_events(event, data.today_weight)
            if not today_weight_pole.active:
                if data.today_weight == '':
                    data.today_weight = 60.0
                else:
                    data.today_weight = float(data.today_weight)

            data.today_height = today_height_pole.check_events(event, data.today_height)
            if not today_height_pole.active:
                if data.today_height == '':
                    data.today_height = 170.0
                else:
                    if float(data.today_height) == 0:
                        data.today_height = 170.0
                    data.today_height = float(data.today_height)

            today_weight_pole.update_pole(screen, settings, data.today_weight)
            today_height_pole.update_pole(screen, settings, data.today_height)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    return_pressed = True

    return back_button_clicked, save_button_clicked, reset_button_clicked, return_pressed


def determine_bmi_result(settings, bmi, flag=0):
    """Определние результата ИМТ"""
    if flag == 1:
        text1 = "Your today's BMI: " + str(bmi)
    else:
        text1 = "Your BMI: " + str(bmi)
    if bmi < 16:
        color = settings.bmi_very_low_color
        text2 = "You are very underweight!"
    elif (bmi >= 16) and (bmi < 18.5):
        color = settings.bmi_low_color
        text2 = "You are underweight."
    elif (bmi >= 18.5) and (bmi <= 25):
        color = settings.bmi_optimal_color
        text2 = "Your weight is optimal!"
    elif (bmi > 25) and (bmi < 30):
        color = settings.bmi_high_color
        text2 = "You are overweight."
    else:
        color = settings.bmi_very_high_color
        text2 = "You are obese! Be careful!"
    return color, text1, text2


def graphs_window(screen, settings, data, back_button, show_bmi_button, show_weight_button):
    """Меню графиков"""
    drawer.draw_graphs_window(screen, settings, back_button, show_bmi_button, show_weight_button)
    back_button_clicked = False
    while not back_button_clicked:
        back_button_clicked, show_bmi_button_clicked, show_weight_button_clicked = \
            check_gw_events(back_button, show_bmi_button, show_weight_button)

        # Графики выводятся только в том случае, если массивы не пустые
        if show_bmi_button_clicked:
            if len(data.dates) > 0:
                graphs.show_bmi_grah(settings, data)
                pygame.event.clear()
            else:
                drawer.draw_text(screen, "No data to show!", settings.screen_width // 2, settings.screen_height - 125,
                                 settings.graph_error_text_color, settings.graph_common_text_font)
        elif show_weight_button_clicked:
            if len(data.dates) > 0:
                graphs.show_weight_graph(data, settings)
                pygame.event.clear()
            else:
                drawer.draw_text(screen, "No data to show!", settings.screen_width // 2, settings.screen_height - 125,
                                 settings.graph_error_text_color, settings.graph_common_text_font)


def loading_window(screen, settings):
    """Окно загрузки"""
    screen.fill(settings.bg_color)
    drawer.draw_text(screen, "Loading...", settings.screen_width // 2, settings.screen_height // 2,
                     settings.main_text_color, settings.main_text_font)
    pygame.display.flip()


def main_menu(screen, settings, data, calculate_bmi_button, calculate_normal_weight_button, graphs_button, today_button,
              exit_button, back_button, calculate_button, show_bmi_button, show_weight_button, save_button,
              reset_button, cnw_height_pole, bmi_height_pole, bmi_weight_pole, today_weight_pole, today_height_pole,
              dialog_window):
    """Главное меню"""
    drawer.draw_main_menu(screen, settings, calculate_bmi_button, calculate_normal_weight_button, graphs_button,
                          today_button, exit_button)
    clock = pygame.time.Clock()

    while True:
        calculate_bmi_button_clicked, calculate_normal_weight_button_clicked, graphs_button_clicked, \
        today_button_clicked = check_main_menu_events(calculate_bmi_button, calculate_normal_weight_button,
                                                      graphs_button, today_button, exit_button)

        if calculate_bmi_button_clicked:
            # Вход в меню расчёта ИМТ
            bmi_window(screen, settings, data, back_button, calculate_button, bmi_height_pole, bmi_weight_pole)
            drawer.draw_main_menu(screen, settings, calculate_bmi_button, calculate_normal_weight_button, graphs_button,
                                  today_button, exit_button)

        elif calculate_normal_weight_button_clicked:
            # Вход в меню расчёта оптимального веса
            cnw_window(screen, settings, data, back_button, calculate_button, cnw_height_pole)
            drawer.draw_main_menu(screen, settings, calculate_bmi_button, calculate_normal_weight_button, graphs_button,
                                  today_button, exit_button)

        elif graphs_button_clicked:
            # Вход в меню графиков
            graphs_window(screen, settings, data, back_button, show_bmi_button, show_weight_button)
            drawer.draw_main_menu(screen, settings, calculate_bmi_button, calculate_normal_weight_button, graphs_button,
                                  today_button, exit_button)

        elif today_button_clicked:
            # Вход в меню ввода данных текущего дня
            today_window(screen, settings, data, back_button, save_button, reset_button, today_weight_pole,
                         today_height_pole, dialog_window)
            drawer.draw_main_menu(screen, settings, calculate_bmi_button, calculate_normal_weight_button, graphs_button,
                                  today_button, exit_button)

        # Задержка с целью экономии ресурсов
        clock.tick(settings.fps)


def check_data(data):
    """Проверка для отрисовки данных сегодняшнего дня"""
    if data.today_nice_date not in data.dates:
        # Данные по умолчанию, если данных текущего дня в массиве нет
        data.today_weight = 60.0
        data.today_height = 170.0

    else:
        # Данные текущего дня
        data.today_weight = data.weights[-1]
        data.today_height = data.heights[-1]


def today_window(screen, settings, data, back_button, save_button, reset_button, today_weight_pole, today_height_pole,
                 dialog_window):
    """Меню ввода данных текущего дня"""
    check_data(data)
    drawer.draw_today_window(screen, settings, data, back_button, save_button, reset_button, today_weight_pole,
                             today_height_pole)
    back_button_clicked = False
    while not back_button_clicked:
        # Меню ввода данных текущего дня активно, пока не нажата кнопка "Back"
        back_button_clicked, save_button_clicked, reset_button_clicked, return_pressed = check_today_window_events(
            screen, settings, data, back_button, save_button, reset_button, today_weight_pole, today_height_pole)

        if save_button_clicked or return_pressed:
            # Срхранение введённых данных
            data.today_bmi = calc_bmi(data.today_height, data.today_weight)
            color, result_text, phrase = determine_bmi_result(settings, data.today_bmi, flag=1)
            drawer.draw_text(screen, result_text, settings.screen_width // 2, settings.screen_height - 250, color,
                             settings.today_common_text_font)
            drawer.draw_text(screen, "Saved!", settings.screen_width // 2, settings.screen_height - 150,
                             settings.today_header_text_color, settings.today_save_text_font)
            pygame.display.flip()
            data.update()
        elif reset_button_clicked:
            # Очистка данных
            drawer.draw_today_window(screen, settings, data, back_button, save_button, reset_button,
                                     today_weight_pole, today_height_pole)

            # Диалоговое окно об уверенности в желании очистить данные
            dialog_window.draw_window()
            yes_button_clicked, no_button_clicked = False, False
            while not (yes_button_clicked or no_button_clicked):
                yes_button_clicked, no_button_clicked = dialog_window.check_events()
            if yes_button_clicked:
                data.reset()

            # Перерисовка меню ввода данных текущего дня
            drawer.draw_today_window(screen, settings, data, back_button, save_button, reset_button, today_weight_pole,
                                     today_height_pole)
