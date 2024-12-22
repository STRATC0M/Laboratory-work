from math import *   
import sys  
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
msg = "Выберите вид функции f(x): \n tg(x) -> 1,\n e**x -> 2, \n pow(x**2,1/3)-> 3 "
f = float(input(msg + "\n -> "))
fx = None
s = None
match f:
    case 1:
        fx = tan(x)
    case 2:
        fx = exp(x)
    case 3:
        fx = pow(x**2,1/3)
    case _:
        print("Неверный выбор")
        sys.exit() # Досрочное завершение программы
if (x * y) > 0:
    s = fabs( fx + y)**2 - pow(fx,3)
elif (x * y) < 0:
    s = fabs((fx + y)**2 - sin(x))
elif (x * y) == 0:
    s = fabs((fx + y)**2 - y**3)
else:
    s = "значение не может быть вычислено"
print("Результат: ", s)
