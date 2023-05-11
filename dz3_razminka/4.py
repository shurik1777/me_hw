'''Игра Скрэббл. На вход подается слово, на выход -
количество баллов, которые можно набрать (попробуйте решить с использованием словаря)
'''
text = input("Введите слово на русском: ").upper()

scrabble = {}

scrabble.update(dict.fromkeys('АВЕИНОРСТ', 1))
scrabble.update(dict.fromkeys('ДКЛМПУ', 2))
scrabble.update(dict.fromkeys('БГЁЬЯ', 3))
scrabble.update(dict.fromkeys('ЫЙ', 4))
scrabble.update(dict.fromkeys('ЖЗХЦЧ', 5))
scrabble.update(dict.fromkeys('ШЭЮ', 8))
scrabble.update(dict.fromkeys('ФЩЪ', 10))

print(f"Очков в слове:  {sum(scrabble[char] for char in text)}")
