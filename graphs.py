from matplotlib import pyplot as plt


def determine_bmi_color(bmi):
    """Определение цвета точки в зависимости от BMI"""
    if bmi < 16:
        color = 'purple'
    elif 16 <= bmi < 18.5:
        color = 'rebeccapurple'
    elif 18.5 <= bmi <= 25:
        color = 'forestgreen'
    elif 25 < bmi <= 30:
        color = 'darkgoldenrod'
    else:
        color = 'red'
    return color


def show_bmi_grah(settings, data):
    """Вывод графика ИМТ"""
    dates_for_levels = [data.dates_for_graphs[0], data.dates_for_graphs[-1]]

    # Уровни для отслеживания
    level_0 = [0, 0]
    level_16 = [16.0, 16.0]
    level_18_5 = [18.5, 18.5]
    level_25 = [25.0, 25.0]
    level_30 = [30.0, 30.0]
    level_40 = [40.0, 40.0]

    # Настройки окна
    fig = plt.figure(dpi=128, figsize=(8, 6))
    fig.canvas.set_window_title(settings.graph_bmi_title)

    # Отрисовка уровней
    plt.plot(dates_for_levels, level_0, c='black')
    plt.plot(dates_for_levels, level_16, c='purple', linewidth=3, alpha=0.7, linestyle='--')
    plt.plot(dates_for_levels, level_18_5, c='rebeccapurple', linewidth=3, alpha=0.7, linestyle='--')
    plt.plot(dates_for_levels, level_25, c='forestgreen', linewidth=3, alpha=0.7, linestyle='--')
    plt.plot(dates_for_levels, level_30, c='darkgoldenrod', linewidth=3, alpha=0.7, linestyle='--')
    plt.plot(dates_for_levels, level_40, c='red', linewidth=3, alpha=0.7, linestyle='--')

    # Заполенение цветом пространства между уровнями
    plt.fill_between(dates_for_levels, level_16, level_0, facecolor='purple', alpha=0.15, label='Very low BMI')
    plt.fill_between(dates_for_levels, level_16, level_18_5, facecolor='rebeccapurple', alpha=0.18, label='Low BMI')
    plt.fill_between(dates_for_levels, level_18_5, level_25, facecolor='forestgreen', alpha=0.15, label='Optimal BMI')
    plt.fill_between(dates_for_levels, level_30, level_25, facecolor='darkgoldenrod', alpha=0.18, label='High BMI')
    plt.fill_between(dates_for_levels, level_30, level_40, facecolor='red', alpha=0.18, label='Very high BMI')

    # Отрисовка графика с точками
    plt.plot(data.dates_for_graphs, data.bmis, linewidth=3, label='Your BMI')
    for i in range(len(data.bmis)):
        color = determine_bmi_color(data.bmis[i])
        plt.scatter(data.dates_for_graphs[i], data.bmis[i], s=40, c=color)

    # Оформление легенды
    plt.legend(loc='lower center', fontsize=15, shadow=True, ncol=3)

    # Оформление графика
    fig.autofmt_xdate()
    plt.title(settings.graph_bmi_title, fontsize=35, c='forestgreen')
    plt.ylabel("Body Mass Index", fontsize=25)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # Показ графика
    plt.show()


def show_weight_graph(data, settings):
    """Вывод графика веса"""
    level_0 = [0 for i in range(len(data.dates_for_graphs))]

    # Настройки окна
    fig = plt.figure(dpi=128, figsize=(8, 6))
    fig.canvas.set_window_title(settings.graph_weight_title)

    # Отрисовка графиков, точек
    plt.plot(data.dates_for_graphs, data.weights, linewidth=3, label='Your weight')

    plt.plot(data.dates_for_graphs, level_0, linewidth=3, c='black')
    plt.plot(data.dates_for_graphs, data.level_16, linewidth=3, c='purple', linestyle='--')
    plt.plot(data.dates_for_graphs, data.level_18_5, linewidth=3, c='rebeccapurple', linestyle='--')
    plt.plot(data.dates_for_graphs, data.level_25, linewidth=3, c='forestgreen', linestyle='--')
    plt.plot(data.dates_for_graphs, data.level_30, linewidth=3, c='darkgoldenrod', linestyle='--')
    plt.plot(data.dates_for_graphs, data.level_40, linewidth=3, c='red', linestyle='--')

    # Заполнение пространства между уровнями
    plt.fill_between(data.dates_for_graphs, level_0, data.level_16, facecolor='purple', alpha=0.15,
                     label='Very low weight')
    plt.fill_between(data.dates_for_graphs, data.level_18_5, data.level_16, facecolor='rebeccapurple', alpha=0.15,
                     label='Low weight')
    plt.fill_between(data.dates_for_graphs, data.level_18_5, data.level_25, facecolor='forestgreen',
                     alpha=0.15, label='Optimal weight')
    plt.fill_between(data.dates_for_graphs, data.level_30, data.level_25, facecolor='darkgoldenrod',
                     alpha=0.2, label='High weight')
    plt.fill_between(data.dates_for_graphs, data.level_30, data.level_40, facecolor='red',
                     alpha=0.15, label='Very high weight')

    # Отрисовка точек
    for i in range(len(data.weights)):
        color = determine_weight_color(data, data.weights[i], i)
        plt.scatter(data.dates_for_graphs[i], data.weights[i], s=40, c=color)

    # Оформление легенды
    plt.legend(loc='lower center', fontsize=15, shadow=True, ncol=3)

    # Оформление графика
    fig.autofmt_xdate()
    plt.title(settings.graph_weight_title, fontsize=40, c='green')
    plt.ylabel('Weight (kg)', fontsize=25)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # Показ графика
    plt.show()


def determine_weight_color(data, weight, i):
    """Определение цвета точки в зависимости от веса"""
    if weight < data.level_16[i]:
        color = 'purple'
    elif data.level_16[i] <= weight < data.level_18_5[i]:
        color = 'rebeccapurple'
    elif data.level_18_5[i] <= weight <= data.level_25[i]:
        color = 'forestgreen'
    elif data.level_25[i] < weight <= data.level_30[i]:
        color = 'darkgoldenrod'
    else:
        color = 'red'
    return color
