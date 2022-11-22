import numpy as np  # Importa libreria especializada en analisis numerico
import matplotlib.pyplot as plt  # Importa libreria de graficos en dos dimensiones
from tabulate import tabulate  # Importa libreria para la creacion de tablas
from math import *  # Importa libreria matematica para python
import sympy as sp  # Importa libreria de matematicas simbolicas


# -----------BISECCION--------------
i = 0  # Se inicializa un valor de x
while i < 4.1:  # Bucle donde se evaluará cada valor de x
    x = sp.symbols('x')  # Se declara la variable simbolica
    f = sp.tan(x)*sp.tanh(x) + 1  # Se declara la funcion
    # Se substituye el valor de x por el valor de i, el incremento
    t = f.subs(x, i)
    # Se imprime el valor de x y el valor de la funcion evaluada en ese punto
    print('En x=', i, 'f(x)=', eval(str(t)))
    i = i+0.1  # Se incrementa el valor del x, para el siguiente ciclo del bucle


def bisec(x1, x2, es, imax):
    xl = x1  # Valor inicial del intervalo de x
    xu = x2  # Valor final del intervalo de x
    xr = (xl + xu)/2  # aproximacion de la raiz de f(x)
    xrv = []  # vector que almacenará xr
    # error(%) se le asigna un valor "grande" para poder empezar el ciclo de iteración
    ea = 2*es
    eav = []  # vector que guarda el error
    niter = 0  # contador de iteraciones
    niterv = []  # vector que guarda las iteraciones
    fxrv = []  # vector que guarda las aproximaciones de f(x)
    bisec_table = []  # tabla de datos

    fxl = f(xl)  # aproximacion de f(x izquierda)
    fxu = f(xu)  # aproximacion de f(x derecha)
    fxr = f(xr)  # aproximacion de f(x raiz)
    fxrv.append(fxr)

    bisec_table.append([])  # primera linea de la tabla para la iteracion 0
    # primera linea de la tabla para la iteracion 0
    bisec_table.append([niter, xl, xu, fxl, fxu, xr, fxr, "--"])

    while ea > es and niter <= imax:  # ciclo controlado por el error maximo y el numero de iteraciones

        xrv.append(xr)
        niter += 1
        niterv.append(niter)

        if fxl*fxr < 0:  # verifica si hay cambio de signo para reordenar xl y xu
            xu = xr
        elif fxl*fxr > 0:
            xl = xr
        else:
            ea = 0

        xrold = xr  # aproximacion anterior a la raiz de f(x)
        xr = (xl + xu)/2  # aproximacion actual a la raiz de f(x)

        if xr != 0:  # Calcula el error
            ea = abs(xr - xrold)
            eav.append(ea)

        fxl = f(xl)  # aproximacion de f(x izquierda)
        fxu = f(xu)  # aproximacion de f(x derecha)
        fxr = f(xr)  # aproximacion de f(x raiz)
        fxrv.append(fxr)

        bisec_table.append([niter, xl, ea])  # agrega datos a la tabla

    print(" ")
    print("Metodo Biseccion")
    print(tabulate(bisec_table, headers=[
          "Iteracion", "Valor de la Raíz", "e absoluto"]))

    print(" ")
    print("Grafica del error")
    plt.plot(niterv, eav, label=("e absoluto"))

    plt.plot()  # llamando grafica

    plt.xlabel("Numero de iteraciones")  # Etiqueta de eje
    plt.ylabel("e absoluto")  # Etiqueta de eje
    # Titulo del grafico
    plt.title("Grafica de e absoluto Vs Numero de Iteraciones")
    plt.legend()  # Leyendas
    plt.show()  # Mostrar grafico

    return ()


# Parametros para controlar las aproximaciones
emax = 10**-6  # Error maximo
itermax = 20  # Numero de iteraciones maximo
x1 = 0  # primer valor inicial de X
x2 = 1  # segundo valor inicial de X
# Valores para graficar la funcion
a = 0  # Valor inicial del rango de x para graficar
b = 1  # Valor final del rango de x para graficar
n = 50  # Cantidad de puntos

# f(x)
# Se generan los valores de x para construir la grafica
x = np.linspace(a, b, n)


def f(xs):
    f_x = np.tan(xs)*np.tanh(xs) + 1  # Funcion
    return (f_x)


fx_table = []  # Tabla de datos de x vs f(x)
cont = 0  # contador
fx = f(x)
for i in range(len(x)):  # Ciclo para llenar la tabla
    fx_table.append([x[i], fx[i]])


bisec(x1, x2, emax, itermax)


# ------------------SECANTE-----------------
def secant(fun, x_a, x_b, iteraciones=20):

    eav = []  # vector que guarda el error
    niterv = []  # vector que guarda las iteraciones
    fxrv = []  # Vector que guarda el valor de la raíz para cada iteración
    x_r = x_b  # Asignación del parametro inicial para el calculo del error
    error = 0  # vector que guarda las aproximaciones de f(x)
    print('Metodo de la secante')
    print(" ")
    print('Iteracion', 'Valor de la Raíz', '      Error')

    # El método de la secante
    while (error < 10**-6):  # Exactitud requerida
        for n in range(iteraciones + 1):  # Bucle de número de iteraciones
            # Cálculo de la secante
            # Ecuacion dle metodo de la secante
            x_n = x_a - fun(x_a)*(x_b - x_a)/(fun(x_b) - fun(x_a))
            error = 0  # Reinicio del error
            error = abs((x_n - x_r)/x_n)  # Calculo y asignación del error
            x_r = x_n  # Guardar la el valor de Xn para el proximo ciclo del bucle
            niterv.append(n+1)  # Guardar el intervalo
            eav.append(error)  # Guardar el error
            print(n+1, '       ', x_n, '    ', error)  # Formato de la tabla
            if fun(x_n) == 0:  # En caso de que se encuentre la raiz exacta
                return x_n
            if fun(x_a) * fun(x_n) < 0:  # En caso de que el valor sea negativo
                x_b = x_n
            else:
                x_a = x_n
        break
    print(" ")
    print("Grafica del error")
    plt.plot(niterv, eav, label=("e absoluto"))
    plt.plot()  # llamando grafica
    plt.xlabel("Numero de iteraciones")  # Etiqueta de eje
    plt.ylabel("e absoluto")  # Etiqueta de eje
    # Titulo del grafico
    plt.title("Grafica de e absoluto Vs Numero de Iteraciones")
    plt.legend()  # Leyendas
    plt.show()  # Mostrar grafico


def g(xs):
    f_x = np.tan(xs)*np.tanh(xs) + 1  # Funcion
    return (f_x)


secant(g, 2, 4,  13)  # Llamado de la función para una exactitud de 10^-6
