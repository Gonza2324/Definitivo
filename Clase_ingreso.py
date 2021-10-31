#importar los modulos
import sympy
from sympy.core.symbol import symbols

#definir variable
q = symbols('q', integer = True)

#Definir clase o plantilla
class Ingreso:
    def __init__(self, precio_de_venta, variable_de_unidad):
        self.precio_de_venta = precio_de_venta
        self.variable_de_unidad = variable_de_unidad
    def Calculo_de_precio_de_venta(self):
        I = self.precio_de_venta * self.variable_de_unidad
        print(I)

Ingreso_1 = Ingreso() #Ingresar la operacion
Ingreso_1.Calculo_de_precio_de_venta()