from sympy import integrate
from sympy.abc import x, C
#Hola hice un cambio
funcion = input('Ingrese la funcion: ')
a = input('Ingrese el valor "a": ')
b = input('Ingrese el valor "b": ')

def Calcular():
    I = integrate(funcion, (x, a, b))
    print(I)
Calcular()
