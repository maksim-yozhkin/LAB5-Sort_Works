import os # модуль для роботи з файловими даними
import re # Модуль для роботи з регулярними виразами

# Функція для сортування слів списку за відповідними правилами:
def filtr_data(list_text: list):
    # Перевірка на коректність обробки символьних даних:
    try:
        list_ciric = [] # Список для слів Кирилиці
        list_latin = [] # Список для слів Латиниці
        sort_text = [] # Список для зберігання відсортованих слів
        # Проходження по отриманому списку слів та визначення як кириличних, так і латинських слів:
        for word in list_text:
            if re.search(r"[\u0400-\u04FF]",word):
                list_ciric.append(word)
            elif re.search(r"[\u0000-\u007F]",word):
                list_latin.append(word)
            else:
                print(f"Визначене слово {word} не містить символів Кирилиці та Латиниці.")
        # Застосування сортування над визначеними символами з вказанням параметра ігнорування регістру:
        list_ciric.sort(key=lambda word: word.lower())
        list_latin.sort(key=lambda word: word.lower())
        sort_text = list_ciric + list_latin # Об'єднання відсортованих категорій слів
        return sort_text
    except Exception as error:
        print(f"При роботі з текстовими даними виникла помилка: {error}")

# Перевірка на коректність відкриття та зчитування текстового файлу:
try:
    # Відкриття текстового файлу з можливістю зчитувати дані:
    with open("text_content.txt", mode="r", encoding="utf-8") as text_file:
        list_text = text_file.read() # Зчитування даних з файлу
        print("Виведення речення текстового файлу: \n")
        print(list_text)
        list_text = re.sub(r"[^\w\s]","",list_text) # Видалення знаків пунктуації з тексту
        list_text = list_text.split() # Розділення тексту на слова
        print("\nПочатковий список слів: \n")
        print(list_text)
        print("\nВідсортований за правилами список слів: \n")
        res = filtr_data(list_text) # Здійснення сортування вказаних даних за правилами
        print(res)
        print(f"\nКількість слів: {len(res)}") # Визначення кількості слів у відсортованому списку
        print("\nОк. Програма успішно завершила свою роботу.")
except IOError as error_1:
    print(f"При зчитуванні файлу виникла помилка: {error_1}")
except Exception as error_1:
    print(f"При спробі вивести речення з текстового файлу виникла помилка: {error_1}")