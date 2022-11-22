# Importar librerias- Desarrollado con anaconda.
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from math import *

# Entre 1 y 5
xi = int(input("Ingresa el intervalo inferior: "))
xf = int(input("Ingresa el intervalo superior: "))  # Se definen los intervalos


Iexacta = 4*(np.exp(xf/4) - np.exp(xi/4) + 2)
print("El resultado exacto de la integral es: ", Iexacta)


def f(x):
    y = np.exp(x/4) + 2
    return y


# Argumentos: funcion (f), intervalo inicial (xi), intervalo final (xf), numero de particiones (n)
def RiemannIzq(f, xi, xf, n):
    # Valores de 'x' en los 'n' intervalos, esta funcion devuelve un arreglo de numeros espaciados igualmente entre los intervalos xi,xf
    x = np.linspace(xi, xf, n)
    A = 0  # Aproximacion del area bajo la curva. Inicia en cero
    a = []  # Vector que guarda el area del rectangulo en cada Subintervalo
    f1 = []  # Valor de la funcion a la izquierda de cada subintervalo
    f2 = []  # Valor de la funcion a la derecha de cada subintervalo
    xbar = []  # Coordenadas en 'x' de las esquinas de cada barra del grafico de barras
    ybar = []  # Coordenadas en 'y' de las esquinas de cada barra del grafico de barras

    for i in range(1, n):
        # Suma de Riemman
        # Evalua la funcion a la izquierda de cada subintervalo y lo agrega al vector 'f1'
        f1.append(f(x[i-1]))
        # Evalua la funcion a la derecha de cada subintervalo y lo agrega al vector 'f1'
        f2.append(f(x[i]))
        fx = f(x[i-1])  # Escoge de 'f(x)' a la izquierda del subintervalo
        # Ancho del subintervalo o rectangulo. En este caso es constante.
        deltax = x[i] - x[i-1]
        # Area del rectangulo del subintervalo y lo agrega el vector 'a'
        a.append(fx*deltax)
        A += fx*deltax  # Suma acumulada del area de los rectangulos para obtener el area bajo la curva aproximada
    return (A, xbar, ybar)


n1 = 8  # Se define el numero de particiones
# Se llama la funcion y sus resultados se asignan a las variables
A1, xbar, ybar = RiemannIzq(f, xi, xf, n1)
e1 = ((Iexacta - A1)/Iexacta)*100  # Se calcula el error

n2 = 20
A2, xbar, ybar = RiemannIzq(f, xi, xf, n2)
e2 = ((Iexacta - A2)/Iexacta)*100

n3 = 400
A3, xbar, ybar = RiemannIzq(f, xi, xf, n3)
e3 = ((Iexacta - A3)/Iexacta)*100

n4 = 3000
A4, xbar, ybar = RiemannIzq(f, xi, xf, n4)
e4 = ((Iexacta - A4)/Iexacta)*100

tabla = [['Suma de Riemann por la izquierda', n1, A1, e1],  # Se declara la variable tabla, donde se imprimiran los datos por medio de la libreria tabulate
         ['', n2, A2, e2],
         ['', n3, A3, e3],
         ['', n4, A4, e4],
         ]


# Se imprime el resultado de la tabla, ingresando como argumentos las cabeceras que llevara
print(tabulate(tabla, headers=["Partición (n)", "Suma Riemann", "Error (%)"]))

# ¿Cuántas particiones requerirá para obtener un error relativo porcentual menor que 0.001?
eMin = 0.001  # Se define el valor minimo de error


def RiemannIzqErrorMenor(f, xi, xf):
    j = 100  # Error inicial, inicializado en 100%
    k = 26220  # Valor inicial de particiones

    while j >= eMin:  # Empieza el bucle, el cual se detendrá cuando el error calculado sea menor al error minimo
        x = np.linspace(xi, xf, k)
        A = 0
        a = []
        f1 = []
        f2 = []
        xbar = []
        ybar = []
        for i in range(1, k):
            # Suma de Riemman (Codigo igual que la funcion original)
            f1.append(f(x[i-1]))
            f2.append(f(x[i]))
            fx = f(x[i-1])
            deltax = x[i] - x[i-1]
            a.append(fx*deltax)
            A += fx*deltax
        j = 0  # La variable J guarda el valor del error en cada iteracion, por lo tanto es reiniciada cada vez que el bucle se ejecuta
        # Se calcula el error para el numero de iteracion
        j = ((Iexacta - A)/Iexacta)*100
        k += 1  # Se añade un rectangulo a la cuenta
        # Imprime el valor del numero de rectangulos de la iteracion y el error ligado a este valor
        print(k, j)

    return (k)


k = RiemannIzqErrorMenor(f, xi, xf)
print('El numero de rectangulos minimo para un error menor a', eMin, 'Es', k)
