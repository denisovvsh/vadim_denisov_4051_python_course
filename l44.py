""" 
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений столбца
unique_values = data['whoAmI'].unique()

# Создание нового DataFrame с колонками для каждого уникального значения
one_hot_encoded = pd.DataFrame(columns=unique_values)

# Заполнение нового DataFrame
for value in unique_values:
    one_hot_encoded[value] = (data['whoAmI'] == value).astype(int)

# Вывод преобразованного DataFrame
print(one_hot_encoded)
