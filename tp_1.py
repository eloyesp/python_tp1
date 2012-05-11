#Nombre de los integrantes del grupo:

create_text(700, 950, "Espinaco - Muga - Olivera", 5, "CENTER")

#Creación de Circulos, colocación de números y colores:

create_circle(500, 500, 150, "Black") #Circulo central.

create_filled_circle(500, 725, 75, "White", "Yellow") #Circulo amarillo.
create_text(500, 725, "1", 10, "CENTER") #Número del circulo.

create_filled_circle(725, 500, 75, "White", "Blue") #Circulo azul.
create_text(725, 500, "2", 10, "CENTER") #Número del circulo.

create_filled_circle(500, 275, 75, "White", "Red") #Circulo rojo.
create_text(500, 275, "3", 10, "CENTER") #Número del circulo.

create_filled_circle(275, 500, 75, "White", "Green") #Circulo verde.
create_text(275, 500, "4", 10, "CENTER") #Número del circulo.

#Datos para ventana de Entrada y Salida:

print "Elija dos circulos (numerados del 1 al 4) para unirlos con una línea." #Explicación para el buen funcionamiento del programa.

x = int(raw_input("Ingrese el número del primer circulo: "))
y = int(raw_input("Ingrese el número del segundo circulo: "))

while (x<1 or x>4 or x==y):
  x = int(raw_input("Vuelva a ingresar un numero entre 1 y 4 para el primer circulo: "))
  
while (y<1 or y>4):
  y = int(raw_input("Vuelva a ingresar un numero entre 1 y 4 para el segundo circulo: "))

if x==1 and y==2 or x==2 and y==1:
  create_line(500, 725, 725, 500, "Black")
elif x==2 and y==3 or x==3 and y==2:
  create_line(725, 500, 500, 275, "Black")
elif x==3 and y==4 or x==4 and y==3:
  create_line(500, 275, 275, 500, "Black")
elif x==4 and y==1 or x==1 and y==4:
  create_line(275, 500, 500, 725, "Black")
elif x==1 and y==3 or x==3 and y==1:
  create_line(500, 725, 500, 275, "Black")
elif x==2 and y==4 or x==4 and y==2:
  create_line(725, 500, 275, 500, "Black")

print "Usted trazó la línea entre los circulos %d y %d." %(x, y)
