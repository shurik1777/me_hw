''' 2. Написать функцию, которая будет возвращать список созданный по заданным критериям:
размер, минимальное и максимальное значение, наличие повторяющихся элементов
Например, на вход вы подаете длину списка - 10, максимальное значение - 500,
 минимальное значение - 0, повторы - False и на выход получаете список
 [132, 0, 11, 45, 476, 7, 98, 38, 345, 61] '''
import random


def back_up(size: int, min_: int, max_: int, repeats: bool) -> tuple[list[int], int, int, bool]:
    nums = random.sample(range(min_, max_ + 1), size) if not repeats else [random.randint(min_, max_) for _ in
                                                                           range(size)]
    return nums, min(nums), max(nums), len(nums) != len(set(nums))

result_size, min_value, max_value, has_repeats = back_up(10, 0, 10, True)
print('Список: ', result_size)
print('Минимальное значение: ', min_value)
print('Максимальное значение: ', max_value)
print('Есть повторы?: ', has_repeats)
