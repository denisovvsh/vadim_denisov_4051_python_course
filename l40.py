""" 
Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
"""

import pandas as pd

# Чтение данных из файла
data = pd.read_csv('sample_data/california_housing_train.csv')

# Фильтрация данных по количеству людей
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# Вычисление средней стоимости дома
mean_house_value = filtered_data['median_house_value'].mean()

print("Средняя стоимость дома, где количество людей от 0 до 500: ", mean_house_value)
