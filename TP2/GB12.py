from math import cos

def aproximacion_coseno(x, decimales):
    x = float(x)
    decimales = int(decimales)
    cos_de_python = cos(x)
    aproximacion = 1.0
    n = 0
    
    def buena_aproximacion(value, expected, decimales):
        print "Diferencia (", value, " - ", expected, ")) = ", abs(value - expected)
        return abs(value - expected) < 10 ** (- decimales)

    def factorial(n):
        resultado = 1
        if n > 1:            
            for i in range(2, n+1):
                resultado *= i
        return resultado
    
    while not buena_aproximacion(aproximacion, cos_de_python, decimales):
        n += 1
        termino = (-1)**(n) * x**(2*n) / factorial(2*n)
        aproximacion += termino
        print "num Termino: ", n
        print "Termino: ", termino
        print "Aproximacion: ", aproximacion

    
    return cos_de_python

resultado = aproximacion_coseno(1, 3)

print "Resultado: ", resultado
print "Aprox (3): ", round(resultado, 3)
