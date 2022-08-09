# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos de "line_plot" de clase

    # Se desea graficar los valores de "x" e "y" en un gráfico de línea
    # A continuación los datos ya disponibles de "x" e "y" para que utilice:
    x = list(range(-10, 11, 1))
    print(x)

    # Bucle que completa y calcula todos los valores de "y"
    y = []
    for i in x:
        y.append(i**2)

    print(y)

    # Alumno: Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "y" en función de "x"

    fig = plt.figure()
    fig.suptitle('parabola_poblacion_ x**2')
    ax = fig.add_subplot()
    ax.plot(x,y, color = 'r', marker = '^', label= 'x^2 (x)')
    ax.set_xlim([0, 2])
    ax.set_ylim([-2, 2])
    ax.legend()
    ax.grid()
    plt.show()
    print('mi primer grafico')


    # Alumno: Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección
    
    # Crear acá su gráfico

    print("terminamos")
