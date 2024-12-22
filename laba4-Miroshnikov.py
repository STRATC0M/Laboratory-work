# Индивидуальное задание
# Ввод строки
input_str = input("Введите строку -> ")

# Замена символов ':' на '%' и подсчет количества замен
replaced_str = input_str.replace(":", "%")
count_replacements = input_str.count(":")

# Вывод результатов
print("Результат замены:", replaced_str)
print("Количество замен:", count_replacements)