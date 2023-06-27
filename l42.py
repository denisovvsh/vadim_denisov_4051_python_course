""" 
Задача 42: Узнать какая максимальная households в зоне минимального значения population
"""

import pandas as pd

# Чтение данных из файла
data = pd.read_csv('sample_data/california_housing_train.csv')

# Нахождение минимального значения population
min_population = data['population'].min()

# Фильтрация данных по минимальному значению population
filtered_data = data[data['population'] == min_population]

# Нахождение максимального значения households
max_households = filtered_data['households'].max()

print("Максимальное значение households в зоне минимального значения population: ", max_households)
