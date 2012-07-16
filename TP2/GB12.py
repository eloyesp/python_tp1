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

#Título del trabajo.

print "Trabajo Practico Numero 2. Tema C."
print "Integrantes: Espinaco-Muga-Olivera."
print "I.S.I. - Comision 'B'"

#Mostramos el Menú:

opcion = 0
opcion2 = ""

while opcion!=4:
  print "\n1) Multiplicacion de 2 numeros enteros."
  print "2) Cambio de base."
  print "3) Calculo de coseno(x), mediante serie."
  print "4) Cerrar programa."
  opcion = int(raw_input("\nEscoja una opcion: "))
  respuesta = "si"

  #Primer inciso:
  if opcion==1:
    while respuesta=="si" or respuesta=="s":
      print "\nEscogio la opcion 1: Multiplicacion de 2 numeros enteros:\n"#Imprime en pantalla la opción elejida.
      x=int(raw_input("Ingrese el primer numero entero: "))#Pide el primer número.
      while x>999999:#Condicion para que no supere los 6 digitos.
        x=int(raw_input("El numero puede tener hasta 6 digitos: "))#Vuelve a pedir en caso de que haya ingresado mal.
      y=int(raw_input("Ingrese el segundo numero entero: "))#Pide el segundo número.
      while y>999999:#Condición para que el número ingresado no supere los 6 digitos.
        y=int(raw_input("El numero puede tener hasta 6 digitos: "))#Vuelve a pedir el número si el usuario ingreso incorrectamente el mismo.
      print "Usted ingreso los numeros %d y %d\n" %(x, y)#Muestra los valores que el usuario ingresó.
      multiplicacion_enteros(x, y)
      respuesta=raw_input("\nQuiere ingresar dos nuevos enteros(si/no)? ")

  #Segundo inciso:
  elif opcion==2:
    #Mostramos el submenú:
    print "\nEscogio la opcion 2: Cambio de base.:"
    print "\na) Cambiar de Decimal a Binario."
    print "b) Cambiar de Binario a Decimal."
    opcion2 = raw_input("\nEscoja opcion a) o b): ")
    while opcion2<"a" or opcion2>"b":#Condición para que solo pueda escojer "a" o "b".
      print "\nSolo puede elegir a) o b)."
      opcion2 = raw_input("Vuelva a intentarlo: ")#En caso de que el usuario haya ingresado otro caracter, vuelve a pedirselo.
    #Inciso "a":
    if opcion2=="a":
      print "\nEscogio la opcion a): Cambiar de Decimal a Binario.:"
      while respuesta=="si" or respuesta=="s":
        print base2(int(raw_input("\nEscriba el numero decimal a convertir: ")))#Pide el número que el usuario desee convertir e imprime el resultado.
        respuesta=(raw_input("\nQuiere convertir otro numero(si/no)? "))#En caso de que quiera convertir otro número tendra que pulsar "si" o "s".
    #Inciso "b":
    elif opcion2=="b":
      print "\nEscogio la opcion b): Cambiar de Binario a Decimal.:"
      while respuesta=="si" or respuesta=="s":
        binario=base10(str(raw_input("\nEscriba un numero en binario: ")))#Pide el número que el usuario desee convertir.
        print "El numero convertido es %d" %(binario)#Imprime el resultado.
        respuesta=(raw_input("\nQuiere convertir otro numero(si/no)? "))#En caso de que quiera convertir otro número tendra que pulsar "si" o "s".

  #Tercer inciso.
  elif opcion==3:
    #Mostramos el submenú:
    print "\nEscogio la opcion 3: Calculo de coseno(x), mediante serie:"
    print "\na) El factorial, representado por !, y el operador de potencia, representado por **, se implementan en el programa mediante funciones."
    print "b) Funcion que no realiza ineficientes llamadas a potencia y factorial."
    opcion2 = raw_input("\nEscoja opcion a) o b): ")
    while opcion2<"a" or opcion2>"b":
      print "Solo puede elegir a) o b)."
      opcion2 = raw_input("Vuelva a intentarlo: ")#En caso de que el usuario haya ingresado otro caracter, vuelve a pedirselo.
    #Inciso "a":
    if opcion2=="a":
      print "\nEscogio la opcion a): El factorial, representado por !, y el operador de potencia, representado por **, se implementan en el programa mediante funciones.:"
      while respuesta=="si" or respuesta=="s":
        x = float(raw_input("Escriba el valor de x: "))#El usuario ingresa el primer parámetro.
        decimales = int(raw_input("Indique la precision deseada (en cantidad de decimales): "))#El usuario ingresa el segundo parámetro.
        print "La aproximacion obtenida es: ", aproximacion_coseno(x, decimales)#Muestra el valor de la función con los parámetros dados por el usuario.
        respuesta=raw_input("\nQuiere escribir otros valores(si/no)? ")
    #Inciso "b":
    elif opcion2=="b":
      print "\nEscogio la opcion b): Funcion exponencial que no realiza ineficientes llamadas a potencia y factorial." 
      while respuesta=="si" or respuesta =="s":
        x = float(raw_input("Escriba el valor de x: "))#El usuario ingresa el primer parámetro.
        decimales = int(raw_input("Indique la precision deseada (en cantidad de decimales): "))#El usuario ingresa el segundo parámetro.
        print "La aproximacion obtenida es: ", aproximacion_coseno_rapida(x, decimales)#Muestra el valor de la función con los parámetros dados por el usuario.
        respuesta=raw_input("\nQuiere escribir otros valores(si/no)? ")

  #Finalización de programa:
  elif opcion == 4:
    print "\nEl programa ha finalizado."#Si el usuario eligió esta opción se termina el programa.

  #Otra opción:
  else:
    print "Ingrese una opcion valida (1, 2, 3 o 4)."#Esto se imprime cuando el usuario no elije una de las opciones dadas en el menú, pide que elija una correcta.
