""" 
Самостоятельная практика №3
Определить какое максимальное и минимальное значение median_house_value
(Доп) Показать максимальное median_house_value, где median_income = 3.1250
(Доп) Узнать какая максимальная population в зоне минимального значения median_house_value
"""

import pandas as pd

# Чтение данных из файла
data = pd.read_csv('sample_data/california_housing_train.csv')

# 1) Определение максимального и минимального значения median_house_value
max_median_house_value = data['median_house_value'].max()
min_median_house_value = data['median_house_value'].min()

print("Максимальное значение median_house_value:", max_median_house_value)
print("Минимальное значение median_house_value:", min_median_house_value)

# 2) Поиск максимального median_house_value, где median_income = 3.1250
max_median_house_value_income = data[data['median_income'] == 3.1250]['median_house_value'].max()

print("Максимальное значение median_house_value при median_income = 3.1250:", max_median_house_value_income)

# 3) Определение максимальной population в зоне минимального значения median_house_value
min_median_house_value = data['median_house_value'].min()
max_population_min_median_house_value = data[data['median_house_value'] == min_median_house_value]['population'].max()

print("Максимальная population в зоне минимального значения median_house_value:", max_population_min_median_house_value)
