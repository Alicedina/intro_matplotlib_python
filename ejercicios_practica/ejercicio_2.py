# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
from turtle import color
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación ya está disponible, es la siguiente:
    x = list(np.linspace(-4, 4, 20))
    y =[]

    y1 = []
    for i in x:
        y1.append(i**2)
    print(y1)

    y2 = []
    for i in x:
        y2.append(i**3)
    print(y2)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, y1, color='b', marker='v', label='y1=i^2')
    ax.plot(x, y2, color='r', marker='>', label='y2=i^3')
    ax.set_facecolor('whitesmoke')
    ax.set_title('funciones cuadratica y cubica')
    ax.set_xlim([0, 2])
    ax.set_ylim([-2, 2])
    ax.legend()
    plt.show(block=False)

    # Alumno: Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico

    print("terminamos")
