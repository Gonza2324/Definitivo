#importar los modulos
import sympy
import numpy as np
from sympy.core.symbol import symbols
#definir la variable
q = symbols('q', integer = True)

#Hacer la clase o plantilla
class Costo:
    def __init__(self, costo_fijo, costo_variable):
        self.costo_fijo = costo_fijo
        self.costo_variable = costo_variable
    def calculo_de_operacion(self):
        operacion = self.costo_fijo + (self.costo_variable * q)
        print(operacion)

Operacion_1 = Costo() #Ingresar la operacion en orden
Operacion_1.calculo_de_operacion()