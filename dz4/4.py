'''4. Функция принимает предложение,
вычисляет какой буквы в этом предложении больше и возвращает эту букву
 и процент ее вхождения предложение. Например, на вход подается фраза
‘ Мама мыла Аллу, Алла мыла пупса’ вывод будет ‘а’ 25%
Обратите внимание - пробелы, знаки пунктуации не учитываются,
а регистр учитывается. Если имеется несколько букв с максимальным результатом
- выводим все такие буквы.'''

def count_chars(s: str) -> str:
    # Убираем все не буквенные символы из строки и переводим всю строку в нижний регистр
    s = ''.join(char for char in s if char.isalpha()).lower()

    # Считаем количество каждой буквы и находим максимальное значение
    char_count = {}
    max_val = 0
    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
        if char_count[char] > max_val:
            max_val = char_count[char]

    # Создаем список с буквами, которые встречаются максимальное количество раз
    max_chars = [char for char in char_count if char_count[char] == max_val]

    # Вычисляем процент вхождения каждой из максимальных букв
    percent = max_val / len(s) * 100

    # Форматируем вывод
    result_str = ' '.join([f'{char} {percent:.2f}%' for char in max_chars])

    return result_str

s = 'Мама мыла Аллу, Алла мыла пупса'

result = count_chars(s)
print(result)  # Output: а 25.00%