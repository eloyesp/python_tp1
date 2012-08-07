from math import cos

#Definimos funciones

# Consigna 1
def multiplicacion_enteros(x, y):
    if x < 10**6 and y >= 0 and y < 10**6:
        print "%12d \nx%11d" %(x,y)
        print "------------"
        #Declaramos variables:
        numero=y%10
        primeramult=numero*x
        numero=(y/10)%10
        segundamult=numero*x
        numero=(y/100)%10
        terceramult=numero*x
        numero=(y/1000)%10
        cuartamult=numero*x
        numero=(y/10000)%10
        quintamult=numero*x
        numero=(y/100000)%10
        sextamult=numero*x
        #Se muestran las multiplicaciones que se van realizando digito por digito (en caso de no haber, solo se imprimen los guiones con un cero a la izquierda).
        print "%12d" % (primeramult)
        print "%11d-" % (segundamult)
        print "%10d--" % (terceramult)
        print "%9d---" % (cuartamult)
        print "%8d----" % (quintamult)
        print "%7d-----" % (sextamult)
        print "------------"
        #Sumamos los valores dados por cada multiplicacion e imprimimos el resultado final.
        sum=(primeramult+(segundamult*10)+(terceramult*100)+(cuartamult*1000)+(quintamult*10000)+(sextamult*100000))
        print "%12d" %(sum)
    elif x < 10**6 and x >= 0 and y < 0:
        print "%16d \nx%15d" %(x,y)
        print "----------------"
        numero=x%10
        primeramult=numero*y
        numero=(x/10)%10
        segundamult=numero*y
        numero=(x/100)%10
        terceramult=numero*y
        numero=(x/1000)%10
        cuartamult=numero*y
        numero=(x/10000)%10
        quintamult=numero*y
        numero=(x/100000)%10
        sextamult=numero*y
        print "%16d" % (primeramult)
        print "%15d-" % (segundamult)
        print "%14d--" % (terceramult)
        print "%13d---" % (cuartamult)
        print "%12d----" % (quintamult)
        print "%11d-----" % (sextamult)
        print "----------------"
        sum=(primeramult+(segundamult*10)+(terceramult*100)+(cuartamult*1000)+(quintamult*10000)+(sextamult*100000))
        print "%16d" %(sum)
    else:
      multiplicacion_enteros(-x, -y)
        
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
