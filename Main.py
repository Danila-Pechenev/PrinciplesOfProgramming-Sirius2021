# -*- coding: utf-8 -*-
"""Main.ipynb

Task 2 of course "Principles of programming" of Sirius January School 2021

Original file is located at
    https://colab.research.google.com/drive/1hxA61xkIRoRNfxg_DfzVsDMNvL1Fa2wi
"""

import pymorphy2
import re

morph = pymorphy2.MorphAnalyzer()

# Тестирующая функция №1 (10 тестов)
def test_form_of_word():
    assert not is_form_of_word('игра', 'Игрушки')
    assert is_form_of_word('игрушек', 'Игрушки')
    assert is_form_of_word('Игрушек', 'Игрушки')
    assert is_form_of_word('решать', 'решаю')
    assert is_form_of_word('читал', 'читавшая')
    assert not is_form_of_word('примерчик', 'пример')
    assert is_form_of_word('примеров', 'примерами')
    assert is_form_of_word('она', 'ею')
    assert is_form_of_word('расти', 'растущий')
    assert not is_form_of_word('программировать', 'программами')

# Проверка, является ли одно слово формой другого
def is_form_of_word(form: str, word: str) -> bool: 
    if morph.parse(form)[0][2] == morph.parse(word)[0][2]:
        return True
    else:
        return False

# Тестируем
test_form_of_word()

# Чтение файла (.txt). Возвращает список строк файла
def read_file(path_to_file: str) -> list: 
    list_of_lines = []
    with open(path_to_file, 'r', encoding='utf-8') as file:
        for line in file:
            list_of_lines.append(line)
    return list_of_lines

# Тестирующая функция №2 (10 тестов)
def test_clean_list_of_lines():
    assert clean_list_of_lines([]) == []
    assert clean_list_of_lines(['']) == [[]]
    assert clean_list_of_lines(['', '']) == [[], []]
    assert clean_list_of_lines(['abc', 'bcd*']) == [['abc'], ['bcd']]
    assert clean_list_of_lines(['●text text, text', 'something here ***']) == [['text', 'text', 'text'], ['something', 'here']]
    assert clean_list_of_lines(['Сириус2021']) == [['Сириус2021']]
    assert clean_list_of_lines(['text:\n']) == [['text']]
    assert clean_list_of_lines(['\ttext']) == [['text']]
    assert clean_list_of_lines(['text; text - text, text']) == [['text', 'text', 'text', 'text']]
    assert clean_list_of_lines(['TeXt...']) == [['TeXt']]

# Чистка списка строк файла от символов, которые будем игнорировать. Формат вывода: список списков слов каждой строки
def clean_list_of_lines(list_of_lines: list) -> list: 
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].replace('\t', '')
        list_of_lines[i] = list_of_lines[i].replace('\r', '')
        list_of_lines[i] = list_of_lines[i].replace('\n', '')
        for symbol in list_of_lines[i]:
            if not symbol.isalnum() and not symbol == ' ':
                list_of_lines[i] = list_of_lines[i].replace(symbol, '')
        list_of_lines[i] = re.sub(" +", " ", list_of_lines[i])
        list_of_lines[i] = list_of_lines[i].split()
    return list_of_lines

# Тестируем
test_clean_list_of_lines()

# Поиск контекста слова и его словоформ с возможностью вывода статистики, морфологического анализа, а также фильтрации
# по морфологическим признакам
def find_сontext_for_one_word(word: str,  # Список слов, словоформы которых будут найдены (list)
                 all_words: list,  # Массив всех слов в тексте по порядку
                 list_of_lines: list,  # Путь до текстового файла (.txt) (str)
                 statistics=True,  # Выводить статистику по количеству найденных слов и словоформ (bool)
                 morphological_analysis=True,  # Выводить морфологический анализ слов (bool)
                 filter_by_morphological_features=False  # Выводить слова, морфологические признаки которых содержат
                                                         # все из перечиселенных в списке признаков.
                                                         # Иначе, False (list or bool)
                ):
    count = 0
    count_exactly_word = 0
    count_forms_of_word = 0
    for i in range(len(list_of_lines)):
        for w in range(len(list_of_lines[i])):
            if is_form_of_word(all_words[count], word): # Проверка, является ли слово словоформой исходного слова
                if (type(filter_by_morphological_features) == list and \
                len(set(str(morph.parse(all_words[count])[0][1]).split(',')) & \
                set(filter_by_morphological_features)) == len(set(filter_by_morphological_features))) \
                or type(filter_by_morphological_features) == bool:  # Проверка на фильтры
                    if all_words[count].lower() == word.lower():
                        count_exactly_word += 1
                    else:
                        count_forms_of_word += 1
                    to_print = []
                    if count >= 2:
                        to_print.append(all_words[count - 2])
                    if count >= 1:
                        to_print.append(all_words[count - 1])
                    to_print.append(all_words[count])
                    if count <= len(all_words) - 2:
                        to_print.append(all_words[count + 1])
                    if count <= len(all_words) - 3:
                        to_print.append(all_words[count + 2])
                    print(f'>> Номер строки: {i + 1}. Контекст: ' + ' '.join(to_print))
                    if morphological_analysis:
                        print('Морфологические признаки: ' + ', '.join(str(morph.parse(all_words[count])[0][1]).split(',')))
                    print('----------------------------------------------')
            count += 1
    if statistics:
        print(f'Найдено {count_exactly_word} слов "{word}" и {count_forms_of_word} словоформ')
    print('______________________________________________')

# Та же функция, но с чтением файла и возможностью поиска нескольких слов
def find_сontext(words: list,  # Список слов, словоформы которых будут найдены (list)
                 path_to_file: str,  # Путь до текстового файла (.txt) (str)
                 statistics=True,  # Выводить статистику по количеству найденных слов и словоформ (bool)
                 morphological_analysis=True,  # Выводить морфологический анализ слов (bool)
                 filter_by_morphological_features=False  # Выводить слова, морфологические признаки которых содержат
                                                         # все из перечиселенных в списке признаков.
                                                         # Иначе, False (list or bool)
                ):
    list_of_lines = clean_list_of_lines(read_file(path_to_file))
    all_words = []
    for i in range(len(list_of_lines)):
        for w in range(len(list_of_lines[i])):
            all_words.append(list_of_lines[i][w])
    for word in words:
        find_сontext_for_one_word(word, all_words, list_of_lines, statistics, 
                                  morphological_analysis, filter_by_morphological_features)

"""Доступные морфологические признаки можно посмотреть здесь:
https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html#grammeme-docs
"""

# Примеры использования и отработки программы можно посмотреть в файле Main.ipynb в репозитории проекта на GitHub,
# протестировать в Google Colab (см. README.md) или здесь:
find_сontext([],  # Указать слова для поиска 
              '', # Указать путь до файла
               statistics=True,
               morphological_analysis=True,
               filter_by_morphological_features=False)
