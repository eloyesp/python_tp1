# -*- coding: UTF-8 -*-
from math import cos

#Definimos funciones

# Consigna 1
def multiplicacion_enteros(x, y):
    if x < 10**6 and y > 0 and y < 10**6 :
        print "%11d \nx%10d" %(x,y)
        print "-----------"
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
        #Se muestran las multiplicaciones que se van realizando digito por digito (en caso de no haber, solo se imprimen los guiones con un cero a la izquierda).
        print "%11d" % (primeramult)
        print "%10d-" % (segundamult)
        print "%9d--" % (terceramult)
        print "%8d---" % (cuartamult)
        print "%7d----" % (quintamult)
        print "-----------"
        #Sumamos los valores dados por cada multiplicación e imprimimos el resultado final.
        sum=(primeramult+(segundamult*10)+(terceramult*100)+(cuartamult*1000)+(quintamult*10000))
        print "%11d" %(sum)
    #En caso de que el "y" sea negativo, intercambiará lugar con la variable "x" y se ejecutara la multiplicación.
    #No supimos resolver en caso de que el usuario ingrese dos números negativos.
    else:
        print "       %14d \n       x%13d" %(x,y)
        print "       --------------"
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
        print "       %14d" % (primeramult)
        print "       %13d-" % (segundamult)
        print "       %12d--" % (terceramult)
        print "       %11d---" % (cuartamult)
        print "       %10d----" % (quintamult)
        print "       --------------"
        sum=(primeramult+(segundamult*10)+(terceramult*100)+(cuartamult*1000)+(quintamult*10000))
        print "       %14d" %(sum)

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

def base10(strn):
  l = len(strn)-1
  result = 0
  for i in strn:
    p = 2**l
    result = result + (int(i)*p)
    l = l-1
  return result

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
