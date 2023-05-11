'''
3. Какой день недели?
Вводим дату и день недели и еще одну дату - программа должна вывести день недели
а) даты в пределах одного месяца
б) одного года
в) даты могут быть любые (с учетом високосности года)
'''
import datetime

def get_weekday(date_str, weekday_str, new_date_str):
    # преобразуем строки в объекты datetime.date
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    weekday = datetime.datetime.strptime(weekday_str, '%Y-%m-%d').date()
    new_date = datetime.datetime.strptime(new_date_str, '%Y-%m-%d').date()
    # определяем номер дня в году для каждой даты
    date_num = date.timetuple().tm_yday
    weekday_num = weekday.timetuple().tm_yday
    new_date_num = new_date.timetuple().tm_yday
    # вычисляем номер столетия
    c = (date.year // 100) - 18
    # вычисляем день недели
    w = (new_date_num + int(2.6 * (new_date.month + 9) % 12 - 0.2) + new_date.year + new_date.year // 4 + c // 4 - 2 * c) % 7
    # выводим ответ в виде строки
    weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    return f'День недели для {new_date}: {weekdays[w]}'

# пример использования
date_str = '2023-05-05'
weekday_str = '2023-05-01'
new_date_str = '2023-05-05'
print(get_weekday(date_str, weekday_str, new_date_str))

# import datetime
# a = datetime.datetime.today().weekday()
# print(datetime.datetime.today())
# if a == 0:
#     print("It's Monday.")
# elif a == 1:
#     print("It's Tuesday.")
# elif a == 2:
#     print("It's Wednesday.")
# elif a == 3:
#     print("It's Thursday.")
# elif a ==4:
#     print("It's Friday.")
# elif a == 5:
#     print("It's Saturday.")
# elif a == 6:
#     print("It's Sunday.")