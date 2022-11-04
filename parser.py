import json # для работы с json файлами
import fitz # используем библиотеку PyMuPDF для парсинга
import re # для работы с рег.выражениями в строках

# переменная для сохранения считанного текста
text = ''
# открываем файл, считываем, сохраняем текст из него в строку
with fitz.open('test_task.pdf') as doc:
    for elem in doc.pages():
        text += elem.get_text()

# чтобы в словарь вошло все вместе с заголовком (отдельная запись), дополним строку
text = 'TITLE: ' + text
# убираем лишние переносы строк из текста
text = text.replace(' \n \n',"\n")
#print(text)

# модификация текста, чтобы выровнять последнюю запись
text_wout_notes = text[:text.find('NOTES') + 6] # срез с удалением лишнего пробела
insp_notes = ' ' + text[text.find('NOTES') + 7:] # срез последней записи в тексте
new_text = text_wout_notes+insp_notes # конкатенация текста и последней записи
#new_text_split = text.split('\n')
print(new_text)


# с помощью рег.выражений модуля 're' формируем пары для словарей из текста
text_reg = re.findall(r'(.+): ((?:.+))', new_text)
# print(text_reg, '\n')
# формируем словарь из списка с кортежами
text_dict = dict((key, value.strip()) for key, value in text_reg)
# print(text_dict, '\n')
# проверка словарей, вывод на экран
print('Текст из файла в виде словарей:\n')
for key, value in text_dict.items():
    print(f'{key}: {value}', end = '\n')

# запись в текстовый файл
file = open('dict_text_out.txt', 'w')
for key, value in text_dict.items():
    file.write(f'{key}: {value}\n')
file.close()

# запись в json
with open("json_out.json", "w") as final:
    json.dump(text_dict, final)
