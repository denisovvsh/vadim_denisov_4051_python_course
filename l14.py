""" Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. """

def print_powers_of_two(N):
    power = 0
    result = 1

    while result <= N:
        print(result)
        power += 1
        result = 2 ** power

N = 50
print("Целые степени двойки, не превосходящие", N, ":")
print_powers_of_two(N)
