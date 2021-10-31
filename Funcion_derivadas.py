#TODO: Proyecto
import numpy
import sympy
from sympy.core.symbol import symbols
x = symbols('x', integrer = True)

def Calculo(Operacion):
    f = sympy.diff(Operacion)
    print(f)
Calculo(Operacion = input(''))