import matplotlib.pyplot as plt 
from modelos import lotka_volt

# En este archivo se hace uso del modelo de Lotka-Volterra

def main():
    #argumentos 

    #ejercicio 1
    a1 = [0.08, 0.1, 0.01, 0.15, 100, 0.2, 0.9]

    #ejercicio 2
    b1 = [0.25, 1.8, 0.91, 0.6, 1000, 0.2, 0.5]

    #ejercicio 3
    c1 = [0.25, 1.1, 0.95, 0.55, 300, 0.2, 0.5]

    list_params = [a1, b1, c1]

    #vamos a generar las graficas caso por caso, creando tres subgraficas.
    for parametros in list_params:
        N, C, Z, punto = lotka_volt(*parametros)

        fig, ax = plt.subplots(1,3, figsize = (15, 5))

        ax[0].plot(N, C, color = 'green')
        ax[0].set_xlabel('n')
        ax[0].set_ylabel('poblacion conejos')

        ax[1].plot(N, Z, color = 'green')
        ax[1].set_xlabel('n')
        ax[1].set_ylabel('poblacion zorros')

        ax[2].plot(C,Z, color = 'green')
        ax[2].set_xlabel('poblacion conejos')
        ax[2].set_ylabel('poblacion zorros')

        if parametros != a1:
            ax[0].scatter(punto[0], punto[1], c='red', zorder = 5, label = 'punto (d/c, r(c-d)/bc)')
            ax[1].scatter(punto[0], punto[1], c='red', zorder = 5, label = 'punto (d/c, r(c-d)/bc)')
            ax[2].scatter(punto[0], punto[1], c='red', zorder = 5, label = 'punto (d/c, r(c-d)/bc)')

        ax[0].legend()
        ax[1].legend()
        ax[2].legend()

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()
