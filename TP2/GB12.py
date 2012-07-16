#Definimos funciones e importo la funcion del coseno(x).
def base2(n):
  result = ""
  while (True):
    aux = str(n%2)
    n = int(n/2)
    result = aux + result
    if (n<=1):
      result = (str(n) if n>0 else "") + result
      break
  return result

def base10(strn):
  l = len(strn)-1
  result = 0
  for i in strn:
    p = 2**l
    result = result + (int(i)*p)
    l = l-1
  return result

from math import cos

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

#T�tulo del trabajo.

print "Trabajo Practico Numero 2. Tema C."
print "Integrantes: Espinaco-Muga-Olivera."
print "I.S.I. - Comision 'B'"

#Mostramos el Men�:

opcion = 0
opcion2 = ""
respuesta="si"
while opcion!=4 and (respuesta=="si" or respuesta=="s"):
  print "\n1) Multiplicacion de 2 numeros enteros."
  print "2) Cambio de base."
  print "3) Calculo de coseno(x), mediante serie."
  print "4) Cerrar programa."
  opcion = int(raw_input("\nEscoja una opcion: "))

  #Primer inciso:
  if opcion==1:
    while respuesta=="si" or respuesta=="s":
      print "\nEscogio la opcion 1: Multiplicacion de 2 numeros enteros:\n"#Imprime en pantalla la opci�n elejida.
      x=int(raw_input("Ingrese el primer numero entero: "))#Pide el primer n�mero.
      while x>999999:#Condicion para que no supere los 6 digitos.
        x=int(raw_input("El numero puede tener hasta 6 digitos: "))#Vuelve a pedir en caso de que haya ingresado mal.
      y=int(raw_input("Ingrese el segundo numero entero: "))#Pide el segundo n�mero.
      while y>999999:#Condici�n para que el n�mero ingresado no supere los 6 digitos.
        y=int(raw_input("El numero puede tener hasta 6 digitos: "))#Vuelve a pedir el n�mero si el usuario ingreso incorrectamente el mismo.
      print "Usted ingreso los numeros %d y %d\n" %(x, y)#Muestra los valores que el usuario ingres�.
      if x<=999999 and (y>0 and y<=999999):#Condiciones de acuerdo a los valores que ingres� el usuario.
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
        #Sumamos los valores dados por cada multiplicaci�n e imprimimos el resultado final.
        sum=(primeramult+(segundamult*10)+(terceramult*100)+(cuartamult*1000)+(quintamult*10000))
        print "%11d" %(sum)
        #En caso de que el "y" sea negativo, intercambiar� lugar con la variable "x" y se ejecutara la multiplicaci�n.
        #No supimos resolver en caso de que el usuario ingrese dos n�meros negativos.
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
      respuesta=raw_input("\nQuiere ingresar dos nuevos enteros(si/no)? ")
    respuesta=(raw_input("\nQuiere escojer otra opcion(si/no)? "))

  #Segundo inciso:
  elif opcion==2:
    #Mostramos el submen�:
    print "\nEscogio la opcion 2: Cambio de base.:"
    print "\na) Cambiar de Decimal a Binario."
    print "b) Cambiar de Binario a Decimal."
    opcion2 = raw_input("\nEscoja opcion a) o b): ")
    while opcion2<"a" or opcion2>"b":#Condici�n para que solo pueda escojer "a" o "b".
      print "\nSolo puede elegir a) o b)."
      opcion2 = raw_input("Vuelva a intentarlo: ")#En caso de que el usuario haya ingresado otro caracter, vuelve a pedirselo.
    #Inciso "a":
    if opcion2=="a":
      print "\nEscogio la opcion a): Cambiar de Decimal a Binario.:"
      while respuesta=="si" or respuesta=="s":
        print base2(int(raw_input("\nEscriba el numero decimal a convertir: ")))#Pide el n�mero que el usuario desee convertir e imprime el resultado.
        respuesta=(raw_input("\nQuiere convertir otro numero(si/no)? "))#En caso de que quiera convertir otro n�mero tendra que pulsar "si" o "s".
      respuesta=(raw_input("\nQuiere escojer otra opcion(si/no)? "))
    #Inciso "b":
    elif opcion2=="b":
      print "\nEscogio la opcion b): Cambiar de Binario a Decimal.:"
      while respuesta=="si" or respuesta=="s":
        binario=base10(str(raw_input("\nEscriba un numero en binario: ")))#Pide el n�mero que el usuario desee convertir.
        print "El numero convertido es %d" %(binario)#Imprime el resultado.
        respuesta=(raw_input("\nQuiere convertir otro numero(si/no)? "))#En caso de que quiera convertir otro n�mero tendra que pulsar "si" o "s".
      respuesta=(raw_input("\nQuiere escojer otra opcion(si/no)? "))

  #Tercer inciso.
  elif opcion==3:
    #Mostramos el submen�:
    print "\nEscogio la opcion 3: Calculo de coseno(x), mediante serie:"
    print "\na) El factorial, representado por !, y el operador de potencia, representado por **, se implementan en el programa mediante funciones."
    print "b) Funcion exponencial que no realiza ineficientes llamadas a potencia y factorial."
    opcion2 = raw_input("\nEscoja opcion a) o b): ")
    while opcion2<"a" or opcion2>"b":
      print "Solo puede elegir a) o b)."
      opcion2 = raw_input("Vuelva a intentarlo: ")#En caso de que el usuario haya ingresado otro caracter, vuelve a pedirselo.
    #Inciso "a":
    if opcion2=="a":
      print "\nEscogio la opcion a): El factorial, representado por !, y el operador de potencia, representado por **, se implementan en el programa mediante funciones.:"
      while respuesta=="si" or respuesta=="s":
        x=int(raw_input("Escriba el valor de x: "))#El usuario ingresa el primer par�metro.
        y=int(raw_input("Escriba el valor de y: "))#El usuario ingresa el segundo par�metro.
        print aproximacion_coseno(x, y)#Muestra el valor de la funci�n con los par�metros dados por el usuario.
        respuesta=raw_input("\nQuiere escribir otros valores(si/no)? ")
      respuesta=(raw_input("\nQuiere escojer otra opcion(si/no)? "))
    #Inciso "b":
    elif opcion2=="b":
      print "\nEscogio la opcion b): Funcion exponencial que no realiza ineficientes llamadas a potencia y factorial." 
      while respuesta=="si" or respuesta =="s":
        x=int(raw_input("Escriba el valor de x: "))#El usuario ingresa el primer par�metro.
        y=int(raw_input("Escriba el valor de y: "))#El usuario ingresa el segundo par�metro.
        print aproximacion_coseno_rapida(x, y)#Muestra el valor de la funci�n con los par�metros dados por el usuario.
        respuesta=raw_input("\nQuiere escribir otros valores(si/no)? ")
      respuesta=(raw_input("\nQuiere escojer otra opcion(si/no)? "))

  #Finalizaci�n de programa:
  elif opcion==4:
    print "\nEl programa se ah finalizado."#Si el usuario eligi� esta opci�n se termina el programa.

  #Otra opci�n:
  else:
    print "Ingrese una opcion valida (1,2,3 o 4)."#Esto se imprime cuando el usuario no elije una de las opciones dadas en el men�, pide que elija una correcta.