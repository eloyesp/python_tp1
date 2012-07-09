from math import cos

def aproximacion_coseno(x, decimales):
    # Inicializacion de las variables
    x = float(x)
    decimales = int(decimales)
    cos_de_python = cos(x)
    aproximacion = 1.0
    n = 0
    
    def buena_aproximacion(value, expected, decimales):
        # print "Diferencia (", value, " - ", expected, ")) = ", abs(value - expected)
        return abs(value - expected) < 10 ** (- decimales)

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
    
    while not buena_aproximacion(aproximacion, cos_de_python, decimales):
        n += 1
        termino = (-1)**(n) * potencia(x, 2*n) / factorial(2*n)
        aproximacion += termino

    return aproximacion

resultado = aproximacion_coseno(1, 5)

print "Resultado: ", resultado
print "cos_de_python: ", cos(1)
