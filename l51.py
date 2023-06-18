""" 
Задача No51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
print(‘same’) else:
print(‘different’) 
"""

#Проверяем, все ли слова списка одинаковой длины
def same_by(characteristic, objects):
    characteristics = [characteristic(obj) for obj in objects]
    return len(set(characteristics)) <= 1

def get_length(word):
    return len(word)

words = ["banana", "cherry"]
result = same_by(get_length, words)
print(result)

""" 
1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.


 пример  - 8 11 0 -23 140 1 => 11 -23
 """

""" list_1 = "8 11 0 -23 140 1".split()
list_2 = list(filter(lambda x: len(str(abs(int(x)))) == 2, list_1))
print(*list_2) """