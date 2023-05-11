''' 1. Дан список чисел. Создать новый список,
который будет содержать только уникальные элементы исходного списка '''

any_list = [1, 3, 3, 4, 2, 5, 5, 4, 2, 1, 1, 3, 4]
print('Дан список чисел\n', any_list)
set_in = set(any_list)  # через функцию set )
list_output = (list(set_in))

print("Уникальные элементы списка"
      " повторяющиеся один раз через функцию множества set():", list_output)

output_list = []
for item in any_list:
    if item not in output_list:
        output_list.append(item)  # через перебор и метод .append + for и if
else:
    print('Уникальные элементы списка повторяющиеся один раз'
          ' через метод append():\n', output_list)


def get_unique_numbers(__iter__):
    unique = []
    for number in __iter__:
        if number not in unique:
            unique.append(number)
    return unique


print('Через вызов функции и метод append: \n', get_unique_numbers(any_list))
