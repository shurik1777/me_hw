""" 1. Написать программу, которая прочитает sample.txt. После этого надо изменить текст,
чтобы каждое предложение было записано с большой буквы (после точки большая буква).
И записать текст обратно в этот файл. Выложить в гит этот файл и файл с самой программой."""

# открываем файл и читаем его содержимое
with open("sample.txt", "r", encoding='UTF=8') as file:
    text = file.read()

# # разбиваем текст на предложения по точкам и удаляем лишние пробелы
# sentences = [str_.strip() for str_ in text.split('.')]
#
# # преобразуем первую букву каждого предложения в заглавную
# result = []
# for str_ in sentences:
#     if len(str_) > 0:
#         result.append(str_[0].upper() + str_[1:])
#
# # соединяем предложения обратно в текст и записываем его в файл
# with open("sample2.txt", "w", encoding='UTF=8') as file:
#     file.write('. '.join(result))
#  еще вариант без срезов с лямбдой
text = text.split('.')
text = list(map(lambda x: x.strip(), text))

with open("sample.txt", "w", encoding='UTF=8') as file:
    text = '. '.join([sentence.capitalize() for sentence in text])
    file.write(text)