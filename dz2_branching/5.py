"""
5. Какого цвета клетка
На вход подается обозначение шахматной клетки, необходимо вывести ее цвет
"""
letter = input('Введите букву шахматной доски от A до H -> ').lower()
digit = int(input('Введите цифру шахматной доски от 1 до 8 -> '))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
digits = range(1, 9)

if letter not in letters:
    print('Нет на шахматной доске такой буквы введите A - H в англ. раскладке')
elif digit not in digits:
    print('Нет такой цифры на шахматной доске интервал от 1го до 8')
else:
    letter_index = letters.index(letter)
    digit_index = digits.index(digit)
    if letter_index % 2 == digit_index % 2:
        print('Черный цвет клетки')
    else:
        print('Белый цвет клетки')