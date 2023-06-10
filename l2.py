""" 
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

number = int(input("Введите трехзначное число: "))

if number >= 100 and number <= 999:
    digit1 = number // 100
    digit2 = (number // 10) % 10
    digit3 = number % 10
    digit_sum = digit1 + digit2 + digit3
    print("Сумма цифр трехзначного числа:", digit_sum)
else:
    print("Введено неверное число. Пожалуйста, введите трехзначное число.")