'''
6. Проверка на палиндром:
а) на вход подается слово - проверить, является ли оно палиндромом
довод, доход, заказ, кабак, комок, мадам, олололо, потоп, радар, ротатор, топот, шалаш
level deified noon Racecar radar repaper
б) на вход подается фраза - проверить, является ли она палиндромом
А роза упала на лапу Азора
Я иду с мечем судия
Хил, худ, а дух лих.
Тарту дорог, как город утрат
А путана тупа
И темен город. Мороз, узором дорог не мети.
Леша на полке клопа нашел.
Аргентина манит негра
Straw? No, too stupid a fad. I put soot on warts
Was it a cat I saw?
Do geese see God?
Madam, I'm Adam
Pull up if I pull up
No lemon, no melon
SATOR AREPO TENET OPERA ROTAS
'''

# my_string = input("Введите слово: ")
# ''' Палиндром или не палиндром по заданию а) через срезы'''
# if str(my_string) == str(my_string)[::-1]:
#     print('Это палиндром')
# else:
#     print('Это не палиндром')

my_string = input("Введите слово: ")
''' Палиндром или не палиндром по заданию б) через срезы плюс коллекцию и перебор'''
my_string = my_string.lower()
wrong = [' ', '`', '`', '!', '?', ',', '.', "'", '\xa0']
for symbol in wrong:
    my_string = my_string.replace(symbol, '')
if str(my_string) == str(my_string)[::-1]:
    print('Это палиндром')
else:
    print('Это не палиндром')
