''' 3. функцию для проверки числа:
  - четность - нечетность
  - простое число (имеет всего два делителя - само себя и единицу)
  - сумма всех цифр числа является делителем этого числа
  - *принимает число и выдает его только простые делители
Это четыре разные функции, но можете объединить в одну '''
num = int(input("Введите число: "))


def even_or_odd(numm) -> str:  # четное не четное
    if numm % 2 == 0:
        return 'Четное число'
    return 'Нечетное число'


print(even_or_odd(num))


def simple_or_note(nums: int) -> str:
    if nums % nums == 0 and nums != 0:
        return 'Простое число'
    return 'Не простое число'


print(simple_or_note(num))


def sum_num(num_: int) -> str | int:
    sum_ = 0
    while num_ != 0:
        sum_ = sum_ + num_ % 10
        num_ = num_ // 10
    return sum_


if num % sum_num(num) == 0:
    print('Является')
else:
    print('Не является')

print(sum_num(num), 'Сумма значений числа')


def simple_divisors(num_: int) -> int:
    for i in range(num_ - 1, 1, -1):
        if num_ % i == 0:
            print(i, end=' ')


print(simple_divisors(num))
