from datetime import date, datetime


class Data:
    """Класс для хранение данных"""

    def __init__(self):
        """Инициализация данных"""
        # Файл, в котором хранится вся информация
        # В файле инфолрмация хранится по следующему порядку: дата, вес, рост, ИМТ...
        # ...вес для ИМТ = 16, 18.5, 25, 30, 40
        self.file_name = 'data.txt'

        # Дата
        self.today_date = date.today()
        string_date = str(self.today_date)
        list_date = string_date.split('-')
        self.today_nice_date = '-'.join(list_date[::-1])

        # Данные для графиков
        self.dates = []
        self.dates_for_graphs = []
        self.weights = []
        self.heights = []
        self.bmis = []
        self.level_16 = []
        self.level_18_5 = []
        self.level_25 = []
        self.level_30 = []
        self.level_40 = []

        try:
            # Если файл найден, то данные считываются
            with open(self.file_name) as f:
                # Получение данных из файла
                for line in f:
                    row = line.split()
                    if len(row) > 0:
                        self.dates.append(row[0])
                        self.dates_for_graphs.append(datetime.strptime(row[0], "%d-%m-%Y"))
                        self.weights.append(float(row[1]))
                        self.heights.append(float(row[2]))
                        self.bmis.append(float(row[3]))
                        self.level_16.append(float(row[4]))
                        self.level_18_5.append(float(row[5]))
                        self.level_25.append(float(row[6]))
                        self.level_30.append(float(row[7]))
                        self.level_40.append(float(row[8]))
        except FileNotFoundError:
            # Если файл не найден, то он создаётся
            open(self.file_name, 'w').close()

        # Данные текущего дня
        if self.today_nice_date not in self.dates:
            # Данные по умолчанию, если данных текущего дня в файле нет
            self.today_weight = 60.0
            self.today_height = 170.0
            self.today_bmi = 20.76

        else:
            # Данные текущего дня
            self.today_weight = self.weights[-1]
            self.today_height = self.heights[-1]
            self.today_bmi = self.bmis[-1]

        # ВрЕменные данные, необходимые для расчёта оптимального веса
        self.cnw_height = 170.0
        self.cnw_min_weight = 54
        self.cnw_max_weight = 72

        # ВрЕменные данные, необходимые для расчёта ИМТ
        self.bmi_weight = 60.0
        self.bmi_height = 170.0
        self.bmi_bmi = 20.76

    def update(self):
        """Обновление данных"""
        if self.today_nice_date not in self.dates:
            # Если данные текущего дня не были сохранены, то они добавляются
            self.dates.append(self.today_nice_date)
            self.dates_for_graphs.append(datetime.strptime(self.today_nice_date, "%d-%m-%Y"))
            self.weights.append(float(self.today_weight))
            self.heights.append(float(self.today_height))
            self.bmis.append(float(self.today_bmi))
            self.level_16.append(self.calc_level_weight(16, self.today_height))
            self.level_18_5.append(self.calc_level_weight(18.5, self.today_height))
            self.level_25.append(self.calc_level_weight(25, self.today_height))
            self.level_30.append(self.calc_level_weight(30, self.today_height))
            self.level_40.append(self.calc_level_weight(40, self.today_height))

            # Вывод данных в файл
            with open(self.file_name, 'a') as f:
                print(self.today_nice_date, float(self.today_weight), float(self.today_height), float(self.today_bmi),
                      self.level_16[-1], self.level_18_5[-1], self.level_25[-1], self.level_30[-1], self.level_40[-1],
                      file=f)
        else:
            # Если данные текущего дня уже были сохранены, они обновляются
            self.weights[-1] = float(self.today_weight)
            self.heights[-1] = float(self.today_height)
            self.bmis[-1] = float(self.today_bmi)
            self.level_16[-1] = self.calc_level_weight(16, self.today_height)
            self.level_18_5[-1] = self.calc_level_weight(18.5, self.today_height)
            self.level_25[-1] = self.calc_level_weight(25, self.today_height)
            self.level_30[-1] = self.calc_level_weight(30, self.today_height)
            self.level_40[-1] = self.calc_level_weight(40, self.today_height)

            # Вывод данных в файл
            with open(self.file_name, 'w') as f:
                for i in range(len(self.dates)):
                    print(self.dates[i], self.weights[i], self.heights[i], self.bmis[i], self.level_16[i],
                          self.level_18_5[i], self.level_25[i], self.level_30[i], self.level_40[i], file=f)

    def reset(self):
        """Очищает данные"""
        self.dates = []
        self.dates_for_graphs = []
        self.weights = []
        self.heights = []
        self.bmis = []
        self.level_16 = []
        self.level_18_5 = []
        self.level_25 = []
        self.level_30 = []
        self.level_40 = []

        open(self.file_name, 'w').close()

    def calc_level_weight(self, level, height):
        """Расчитывает вес, соответствующий определнному уровню ИМТ согласно таблице"""
        height = float(height) / 100
        weight = round((level * (height ** 2)), 2)
        return weight
