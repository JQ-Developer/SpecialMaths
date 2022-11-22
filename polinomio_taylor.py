import numpy as np  # Importa libreria especializada en analisis numerico
import matplotlib.pyplot as plt  # Importa libreria de graficos en dos dimensiones
from tabulate import tabulate  # Importa libreria para la creacion de tablas
from math import *  # Importa libreria matematica para python
import sympy as sp  # Importa libreria de matematicas simbolicas

ft = 'sp.exp(-2*x)*x**2'  # Funcion a evaluar en el polinomio de Taylor
valor = eval('sp.exp(-2*0.3)*0.3**2')  # Valor de la funcion

print(valor)


def PolTaylor(a, n, ft):
    # Se define la variable a trabajar, en este caso se usa symbols para que python sepa que es una variable matematica
    x = sp.symbols('x')
    f = sp.exp(-2*x)*x**2  # Se introduce la funcion
    F = f
    # Se substituyen las variables en la funcion introducidas, x por a
    T = f.subs(x, a)
    for k in range(1, n+1):  # Se inicializa el bucle que generará el polinomio, el cual ira desde 1 hasta n-1, que se traduce en 0 hasta el orden deseado
        dfk = sp.diff(f, x)  # Se calcula la derivada
        T = T+dfk.subs(x, a)*((x-a)**k)/factorial(k)  # Se genera el polinomio
        f = dfk  # A la función se le asigna la nueva derivada
    x = 0.3  # Se introduce el valor de x a evaluar
    polinomio = T  # Se le asigna el valor al polimonio, T es que se acaba de calcular
    polinomio_evaluado = eval(str(T))  # Se evalua el polinomio generado
    # Se calcula el error de truncamiento
    error_de_truncamiento = eval(ft) - eval(str(T))

    # Se regresan los valores requeridos
    return (polinomio, polinomio_evaluado, error_de_truncamiento)


# Polinomio de orden 0
# Se llama el polinomio con los parametros deseados, el valor de a, el orden y la funcion
pol_0, pol_0_eval, error_0 = PolTaylor(0, 0, ft)
print(pol_0)
print(error_0)

# Orden 1
pol_1, pol_1_eval, error_1 = PolTaylor(0, 1, ft)
print(pol_1)
print(error_1)

# Orden 2
pol_2, pol_2_eval, error_2 = PolTaylor(0, 2, ft)
print(pol_2)
print(error_2)
# Orden 3
pol_3, pol_3_eval, error_3 = PolTaylor(0, 3, ft)
print(pol_3)
print(error_3)
# Orden 4
pol_4, pol_4_eval, error_4 = PolTaylor(0, 4, ft)
print(pol_4)
print(error_4)
# Orden 5
pol_5, pol_5_eval, error_5 = PolTaylor(0, 5, ft)
print(pol_5)
print(error_5)


tabla = [['0', pol_0, error_0, pol_0_eval],  # Se declara la variable tabla, donde se imprimiran los datos por medio de la libreria tabulate
         ['1', pol_1, error_1, pol_1_eval],
         ['2', pol_2, error_2, pol_2_eval],
         ['3', pol_3, error_3, pol_3_eval],
         ['4', pol_4, error_4, pol_4_eval],
         ['5', pol_5, error_5, pol_5_eval],
         ]


# Se imprime el resultado de la tabla, ingresando como argumentos las cabeceras que llevara
print(tabulate(tabla, headers=["Grado del Polinomio", "Polinomio de Taylor Generado",
      "Error de Truncamiento", "Evaluación del Polinomio"]))
