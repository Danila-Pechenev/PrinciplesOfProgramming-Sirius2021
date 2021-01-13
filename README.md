# Principles_of_programming_TASK2
Task 2 of course "Principles of programming" of Sirius January School 2021

### Автор решения: Печенев Данила Евгеньевич  
Постановка задачи: Дан текстовый файл, содержащий текст свободного формата на русском языке, и некоторое слово. Необходимо найти все вхождения этого слова или любых его словоформ и вывести их в контексте (вместе с двумя словами до и двумя словами после, а также номером строки в файле), игнорируя знаки препинания и переводы строк.  
В качестве файлов для тестирования решения отлично подходят текстовые файлы с сайта lib.ru.  
### Расширение постановки задачи
● вызможность находить не одно слово и словоформы, а несколько  
● возможность вывода статистики по количеству найденных слов и словоформ  
● возможность вывод морфологического анализа слов  
● возможность фильтрации слов по морфологическим признакам (например, пользователя интересуют только прилагательные, а другого пользователя только существительные именительного падежа)  
### Как использовать программу  
Посмотреть на то, как отработала программа на трех тестах можно, открыв файл Main.ipynb в GitHub. Если необходимо протестировать программу на своих тестах, читать дальше.  
Предлагаем два варианта для того, чтобы протестировать программу:  
1 способ. Запустить файл Main.py  
Сначала необходимо установить библиотеки:  
● pymorphy2   
● pymorphy2-dicts  
● DAWG-Python  
Чтобы запустить программу необходимо вызвать функцию find_сontext и передать следующие параметры:  
● words - список слов, словоформы которых будут найдены (list)  
● path_to_file - путь до текстового файла (.txt) (str)  
● statistics=True - выводить статистику по количеству найденных слов и словоформ (bool)  
● morphological_analysis=True - выводить морфологический анализ слов (bool)  
● filter_by_morphological_features=False - выводить слова, морфологические признаки которых содержат все из перечиселенных в списке признаков. Если нет необходимости, False (list or bool)  
Доступные морфологические признаки можно посмотреть здесь:  
https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html#grammeme-docs  
2 способ. Открыть файл Main.ipynb в среде Google Colab и запустить все ячейки, кроме тестов функции find_сontext (чтобы они сработали, необходимо подгрузить тестовые файлы и указать для них пути):  
https://drive.google.com/file/d/1hxA61xkIRoRNfxg_DfzVsDMNvL1Fa2wi/view?usp=sharing  
Чтобы протестировать программу на своих тестах необходимо вызвать функцию find_сontext и передать ей параметры, описанные в предыдущем пункте.  
