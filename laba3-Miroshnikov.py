import math

# Исходные данные
x1 = 1
xn = 4
dx = 0.2
a = 3.5
b = 1.2

# Вычисление с использованием цикла while
print("\n Результаты с использованием цикла while:")
x = x1
while x <= xn:
    y = math.sqrt(a * x) / (b + a * math.sqrt(x))
    print(f"x = {x:.2f}, y = {y:.4f}")
    x += dx


import math

# Исходные данные
x1 = 1
xn = 4
dx = 0.2
a = 3.5
b = 1.2

# Вычисление с использованием цикла for
print("Результаты с использованием цикла for:")
for i in range(int((xn - x1) / dx) + 1):  # +1 для включения xn
    x = x1 + i * dx
    y = math.sqrt(a * x) / (b + a * math.sqrt(x))
    print(f"x = {x:.2f}, y = {y:.4f}")