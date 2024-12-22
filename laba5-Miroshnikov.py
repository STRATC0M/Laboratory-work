# Лаб работа №5
# Задание 1
numbers = input('Введите целые числа через пробел: ', ).split()
numbers = [int(num) for num in numbers]

numbers.reverse()
max_num = max(numbers)

print('Максимальный элемент в списке: ', max_num, '\nСписок в обратном порядке: ', numbers)


# Задание 2
numbers = input('Введите целые числа через пробел: ', ).split()
numbers = [int(num) for num in numbers]

avg = sum(numbers) / len(numbers)

for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers[i] = avg

print('Результат: ', numbers)