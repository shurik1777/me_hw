"""2. Выдать топ 5 самых встречаемых слов в Алисе
файл 'Alice_in_Wonderland.txt'
длинна которых не меньше 5 букв.
Так же можете собрать еще какую-то статистику
(не обязательное задание на фантазию)."""
from string import punctuation
with open("Alice_in_Wonderland.txt", "r", encoding='UTF=8') as file:
    text = file.read()
# print(text)
# проверка длины слов и добавления их в список
"""result = []
words = text.split()
for word in words:
    if len(word) > 5:
        result.append(word)
print(result)"""
