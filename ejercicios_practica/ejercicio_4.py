# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
from socket import AF_X25
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    ax1.plot(x, y1, color='b', marker='v', label='y= x^2')
    ax1.set_facecolor('whitesmoke')
    ax1.set_title('cuadratica')
    ax1.set_ylabel('eje Y')
    ax1.set_xlabel('eje X')
    ax1.set_xlim([0, 2])
    ax1.set_ylim([-2, 2])
    ax1.legend()


    ax2.plot(x, y2, color='r', marker='>', label='y = x^3')
    ax2.set_facecolor('whitesmoke')
    ax2.set_title('cubica')
    ax2.set_ylabel('eje Y')
    ax2.set_xlabel('eje X')
    ax2.set_xlim([0, 3])
    ax2.set_ylim([-4, 2])
    ax2.legend()

    ax3.plot(x, y3, color='k', marker='.', label='y = x^4')
    ax3.set_facecolor('whitesmoke')
    ax3.set_title('a la cuarta')
    ax3.set_ylabel('eje Y')
    ax3.set_xlabel('eje X')
    ax3.set_xlim([0, 2])
    ax3.set_ylim([-2, 2])
    ax3.legend()



    ax4.plot(x, y4, color='lime', marker='^', label='y = raiz^2')
    ax4.set_facecolor('whitesmoke')
    ax4.set_title('raiz cuadrada')
    ax4.set_ylabel('eje Y')
    ax4.set_xlabel('eje X')
    ax4.set_xlim([0, 2])
    ax4.set_ylim([0, 1])
    ax4.legend()

    plt.show()
    
    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico

    print("terminamos")
