from math import cos

# Aproxima el coseno a partir de una serie de Taylor, para un valor de x
# (float), la serie se evalua hasta que la diferencia con el valor dado por
# python es equivalente en los primeros n decimales.

def aproximacion_coseno(x, decimales):
    # Inicializacion de las variables
    x = float(x)
    decimales = int(decimales)
    cos_de_python = cos(x)
    aproximacion = 1.0
    n = 0
    
    def buena_aproximacion(value, expected, decimales):
        return abs(value - expected) < 10 ** (- decimales)

    # Factorial y potencia se calculan utilizando funciones.
    def factorial(n):
        resultado = 1
        if n > 1:            
            for i in range(2, n+1):
                resultado *= i
        return resultado

    def potencia(x, n):
        resultado = 1
        if n > 0:
            for i in range(n):
                resultado *= x
        return resultado

    # Se mejora la aproximacion hasta ser "buena".
    while not buena_aproximacion(aproximacion, cos_de_python, decimales):
        n += 1
        termino = potencia(-1, n) * potencia(x, 2*n) / factorial(2*n)
        aproximacion += termino

    return aproximacion

# Equivalente a la anterior pero más eficiente, ya que no realiza llamados a
# funcion y no calcula repetidamente las multiplicaciones.

def aproximacion_coseno_rapida(x, decimales):
    # Inicializacion de las variables
    x = float(x)
    decimales = int(decimales)
    cos_de_python = cos(x)

    numerador = 1.0
    denominador = 1
    signo = 1
    aproximacion = 1.0
    n = 0
        
    while abs(aproximacion - cos_de_python) > 10 ** (- decimales):
        n += 1
        numerador *= x * x
        denominador *= (2*n - 1) * (2*n)
        signo *= (-1)
        termino = signo * numerador / denominador
        aproximacion += termino
        
    return aproximacion


# Aca probamos las funciones para ver como funcionan...

from time import clock

benchmark = clock()

for x in (0, 1, 5, -5, 10, 20):
    for n in (3, 5, 8):
        resultado = aproximacion_coseno(x, n)
        print "Resultado: ", resultado
        print "Cos_de_py: ", cos(x)

print "benchmark: ", clock() - benchmark
benchmark = clock()

for x in (0, 1, 5, -5, 10, 20):
    for n in (3, 5, 8):
        resultado = aproximacion_coseno_rapida(x, n)
        print "Resultado: ", resultado
        print "Cos_de_py: ", cos(x)

print "benchmark: ", clock() - benchmark
