""" 
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  
"""

def check_rhythm(text):
    #Разделение стихотворения на фразы
    phrases = text.split()
    vowel_count_old = 0
    #Проверка ритма для каждой фразы
    for phrase in phrases:
        #Разделение фразы на слова
        words = phrase.split("-")
        #Подсчет гласных букв
        vowel_count = len([c for word in words for c in word if c.lower() in 'аеёиоуыэюя'])
        #Если количество гласных букв не совпадает с количеством слов
        if vowel_count_old > 0 and vowel_count != vowel_count_old:
            #Ритм нарушен
            return "Пам парам"
        vowel_count_old = vowel_count
    #Ритм соблюден
    return "Парам пам-пам"

text = "пара-ра-рам рам-пам-папам па-ра-па-да"
result = check_rhythm(text)
print(result)