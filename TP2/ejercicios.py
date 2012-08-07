from math import cos

#Definimos funciones

# Consigna 1
def multiplicacion_enteros(x, y):
    # Calculo la cantidad de digitos de x e y
    digitos_x = len(str(x))
    digitos_y = len(str(y))

    # Si el signo es negativo agrego un digito mas.
    signo = 1
    if (x < 0):
        digitos_x += 1
        signo *= -1
    if (y < 0):
        digitos_y += 1
        signo *= -1

    ancho = max(digitos_x + digitos_y, digitos_y + 2)

    # Imprime la operacion a realizar
    print ""
    print "%*d" % (ancho, x)
    print "x %*d" % (ancho - 2, y)
    if (y != 0):
        print "-" * ancho

    guiones = 0
    suma = 0
    x = abs(x)
    y = abs(y)
    
    # Imprime los renglones del medio
    while (y != 0):
        parcial = x * (y % 10)
        y = y / 10
        print "%*d%s" % (ancho - guiones, parcial, "-" * guiones)
        suma += parcial * 10**guiones
        guiones += 1

    # Imprime el resultado
    suma = suma * signo
    print "-" * ancho
    print "%*d" % (ancho, suma)
    
    return suma
        
# Consigna 2 - inciso 'a'
def base2(n):
    if n == 0: # caso base
        resultado = "0"
    elif n == 1: # caso base para evitar el cero a la izquierda
        resultado = "1"
    elif n > 1:
        resultado = base2(n / 2) + str(n % 2)
    else:
        resultado = "- " + base2(-n)
    return resultado

def base10(binario):
  binario = int(binario)
  if (binario < 0):
    return -2
  decimal = 0
  exponente = 0
  while (binario != 0):
    resto = binario % 10
    binario = binario / 10
    if (resto == 0):
      decimal # no hago nada
    elif (resto == 1):
      decimal += 2**exponente
    else:
      return -1
    exponente += 1
  return decimal

def aproximacion_coseno(x, decimales):
    # Inicializacion de las variables
    x = float(x)
    decimales = int(decimales)
    cos_de_python = cos(x)
    aproximacion = 1.0
    n = 1
    
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
        termino = potencia(-1, n) * potencia(x, 2*n) / factorial(2*n)
        aproximacion += termino
        n += 1

    print "Se calcularon %i terminos de la serie" % n
    return aproximacion

def aproximacion_coseno_rapida(x, decimales):
    # Inicializacion de las variables
    x = float(x)
    decimales = int(decimales)
    cos_de_python = cos(x)

    numerador = 1.0
    denominador = 1
    signo = 1
    aproximacion = 1.0
    n = 1
        
    while abs(aproximacion - cos_de_python) > 10 ** (- decimales):
        numerador *= x * x
        denominador *= (2*n - 1) * (2*n)
        signo *= (-1)
        termino = signo * numerador / denominador
        aproximacion += termino
        n += 1

    print "Se calcularon %i terminos de la serie" % n    
    return aproximacion
