# 4. На вход поступает десятичное число, вывести его в виде двоичного.
number_in = int(input('Введите десятичное число: '))

line_result = ''

while number_in > 0:
    line_result = str(number_in % 2) + line_result
    number_in = number_in // 2

print('Результат в двоичном виде:', line_result)
