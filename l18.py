""" Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

def find_closest_element(array, x):
    closest_element = array[0]
    min_difference = abs(x - closest_element)

    for num in array:
        difference = abs(x - num)
        if difference < min_difference:
            closest_element = num
            min_difference = difference

    return closest_element

# Считываем количество элементов в массиве
n = int(input("Введите количество элементов в массиве: "))

# Считываем элементы массива
array = []
for _ in range(n):
    num = int(input("Введите элемент массива: "))
    array.append(num)

# Считываем число X
x = int(input("Введите число X: "))

# Вызываем функцию find_closest_element для поиска ближайшего элемента
closest = find_closest_element(array, x)

# Выводим результат
print(f"Ближайший элемент к числу {x} в массиве: {closest}.")
