'''Функции
1. Написать функцию, которая принимает на вход строку из
рандомных цифр и букв, а возвращает:
  а) строку только из букв
Пример:
На вход подается строка ’я купила 143 апельсина за 545 рублей’, мы должны получить ‘якупилаапельсиназарублей’
 б) строку только из цифр
А тут вернет ’143545’
  в) сравнить длину строк из цифр и из букв и вернуть ту, которая длиннее
'''

my_str = 'я купила 14 апельсина за 545 рублей'


def process_string(string_: str) -> str:
    numeric = ''
    alpha = ''
    for char in string_:
        if char.isnumeric():
            numeric += char
        elif char.isalpha():
            alpha += char

    if len(numeric) > len(alpha):
        return numeric
    else:
        return alpha

result = process_string(my_str)
print(result)