

def lotka_volt(r: float, c: float, b: float, d: float, n: int,  Co: float, Zo: float):
    """
    Funcion que modela el sistema de Lotka-Volterra (depredador-presa).

    Args:
        r (float): Tasa de crecimiento de los conejos (presa).
        c (float): Tasa de éxito en la caza que beneficia a la población de
            zorros (depredador).
        b (float): Tasa de éxito en la caza que reduce la población de
            conejos (presa).
        d (float): Tasa de mortalidad/decrecimiento de los zorros.
        n (int): Número de iteraciones del sistema.
        Co (float): Población inicial de conejos.
        Zo (float): Población inicial de zorros.

    Returns:
        tuple: Una tupla (N, C, Z, punto) donde:
            N (list[int]): Índices de iteración, de 0 a n.
            C (list[float]): Población de conejos en cada iteración
                (longitud n+1).
            Z (list[float]): Población de zorros en cada iteración
                (longitud n+1).
            punto (tuple[float, float]): Punto de equilibrio no trivial del
                sistema, (d/c, r(c-d)/(b*c)).
    """

    #valores iniciales
    C = [Co]
    Z = [Zo]
    N = [0]

    #hacemos el algoritmo n veces
    for _ in range(n):
        Cn = C[-1]
        Zn = Z[-1]

        C.append( (r+1)*Cn - r*Cn**2 - b*Cn*Zn )
        Z.append( c*Zn*Cn + (1-d)*Zn )
        N.append(_)

    #este punto nos lo piden en dos ejercicios 
    punto = (d/c, (r*(c-d))/(b*c))    

    return N, C, Z, punto 
