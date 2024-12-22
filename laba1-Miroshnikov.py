import math as mp
x = int(input("Введите значениие x->"))  
y = int(input("Введите значениие y->"))
z = int(input("Введите значениие z->"))
def calculate_S(x,y,z):
    a1 = cosiane_part = 2 * mp.cos(x-2/3)
    a2 = sine_part= 1/2 + mp.sin(y)**2
    a3 = fraction_part = z**2 / (3-z**2/5)
    S = (a1/a2)*(1+a3)
    return S 
result = calculate_S(x,y,z)
print(f"Значение S:{result}")
