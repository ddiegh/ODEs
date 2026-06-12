# Practica 4. Sistema de ecuaciones en diferencia: Modelo presa-depredador

# Integrantes:
* Sánchez Ramírez Diego Alberto
* Góngora Ramírez Arturo

# Introduccion: 
En esta practica implementamos el modelo de depredador-presa de Lotka-Volterra en el que interactuan dos especies, en este caso: conejos y zorros. 

Nos interesa ver como evoluciona el sistema en el tiempo dependiendo de los parametros con los que usemos el modelo.

### Modelo matemático

El sistema se define mediante las siguientes ecuaciones en diferencias:

$$
\begin{aligned}
C_{n+1} &= (r+1)\,C_n - r\,C_n^2 - b\,C_n Z_n \\
Z_{n+1} &= c\,Z_n C_n + (1-d)\,Z_n
\end{aligned}
$$

donde $C_n$ y $Z_n$ son las poblaciones de conejos y zorros en la iteración $n$.

#### Parámetros

| Símbolo | Significado |
|---------|-------------|
| $r$ | Tasa de crecimiento de los conejos (presa). |
| $c$ | Tasa de éxito en la caza que beneficia a la población de zorros. |
| $b$ | Tasa de éxito en la caza que reduce la población de conejos. |
| $d$ | Tasa de decrecimiento de los zorros. |
| $n$ | Número de iteraciones del sistema. |
| $C_0$ | Población inicial de conejos. |
| $Z_0$ | Población inicial de zorros. |

### Punto de equilibrio

El sistema posee un punto de equilibrio dado por:

$$
\left( \frac{d}{c},\; \frac{r(c-d)}{bc} \right)
$$

Este punto se marca en rojo sobre las gráficas en las que se nos pide.

## Requisitos
- `matplotlib.pyplot`

```bash
pip install matplotlib
```

## Ejecución

```bash
1. modelos.py
2. main.py
```
## Uso

La función principal es `lotka_volt` la cual es el modelo del sistema. Recibe los parámetros y devuelve los valores de como evolucionó el sistema, junto con el punto de equilibrio:

```python
N, C, Z, punto = lotka_volt(r, c, b, d, n, Co, Zo)
```

| Salida | Descripción |
|--------|-------------|
| `N` | Índices de iteración. |
| `C` | Población de conejos en cada iteración. |
| `Z` | Población de zorros en cada iteración. |
| `punto` | Punto de equilibrio $(d/c,\; r(c-d)/bc)$. |

La función `main` recorre tres conjuntos de parámetros (un ejercicio cada uno) y
genera, para cada caso, tres subgráficas:

1. **Conejos vs. iteración** ($n$ contra $C_n$).
2. **Zorros vs. iteración** ($n$ contra $Z_n$).
3. **Plano fase** ($C_n$ contra $Z_n$).

## Analisis

| Ejercicio | $r$ | $c$ | $b$ | $d$ | $n$ | $C_0$ | $Z_0$ |
|-----------|-----|-----|-----|-----|-----|-------|-------|
| 1 | 0.08 | 0.10 | 0.01 | 0.15 | 100 | 0.2 | 0.9 |
| 2 | 0.25 | 1.80 | 0.91 | 0.60 | 1000 | 0.2 | 0.5 |
| 3 | 0.25 | 1.10 | 0.95 | 0.55 | 300 | 0.2 | 0.5 |


> En el ejercicio 1 no se nos pide graficar el punto de equilibrio

![Imagen 1](/practica4/imagenes/Figure_1.png)

En este caso vemos un crecimiento de conejos sobre los de zorros y esto se lo podemos deber al los valor $ c = 0.10$ y a $b=0.01$ ya que estos valores influyen fuertemente a como van a progresar los conejos y los zorros. 
Al mismo tiempo que vemos como los conejos crecen, podemos verlo de forma dual en los zorros, con ellos decreciendo. 


![Imagen 2](/practica4/imagenes/Figure_2.png)
Aquí con $c = 1.8$ y $b = 0.91$ las dos poblaciones se mantienen oscilando todo el tiempo, sin que las oscilaciones se hagan más chicas. Cada vez que suben los conejos, poco después suben los zorros, y cuando hay muchos zorros los conejos vuelven a bajar, así que nunca se asientan en un valor fijo.
Esto lo podemos ver muy claro en el plano fase, donde la trayectoria forma una órbita cerrada que da vueltas alrededor del punto de equilibrio sin llegar a tocarlo.

![Imagen 3](/practica4/imagenes/Figure_3.png)
En este último caso, con $c = 1.1$ y $d = 0.55$, las poblaciones también empiezan oscilando pero cada vez con menos fuerza, hasta que se quedan quietas en un valor constante.
En el plano fase esto se ve como una espiral que se va cerrando hacia adentro y termina justo en el punto de equilibrio (el punto rojo), lo que podemos interpretar como que conejos y zorros terminan coexistiendo de forma estable.
 
## Conclusion 
Con los ejemplos de uso podemos ver que los valores con los que usamos el modelo influyen mucho en como se va a desarrollar la dinamica del sistema. Igual podemos ver que el sistema funciona bien en distintos casos. 