# Trabajo Práctico Nº1. Grupo 12 - Tema "A". Comisión "B"
# Expresiones aritméticas, Funciones Matemáticas, Gráficos.

# Nombre de los integrantes del grupo:

create_text(700, 950, "Espinaco - Muga - Olivera", 5, "CENTER") #Se muestra en la pantalla gráfica.

# Creación de Circulos, colocación de números y colores:

create_circle(500, 500, 150, "Black") # Circulo central.

create_filled_circle(500, 725, 75, "White", "Yellow") # Circulo amarillo.
create_text(500, 725, "1", 10, "CENTER") # Número del circulo.

create_filled_circle(725, 500, 75, "White", "Blue") # Circulo azul.
create_text(725, 500, "2", 10, "CENTER") # Número del circulo.

create_filled_circle(500, 275, 75, "White", "Red") # Circulo rojo.
create_text(500, 275, "3", 10, "CENTER") # Número del circulo.

create_filled_circle(275, 500, 75, "White", "Green") # Circulo verde.
create_text(275, 500, "4", 10, "CENTER") # Número del circulo.

# Datos para ventana de Entrada y Salida:

print "Elija dos circulos (numerados del 1 al 4) para unirlos con una línea.\n" # Explicación para el buen funcionamiento del programa.

x = round(float(raw_input("Ingrese el número del primer circulo: "))) # El usuario ingresa el primer dato. Si se escribe un número con decimales, lo redondeará.
while (x<1 or x>4):
  x = round(float(raw_input("Vuelva a ingresar un número entre 1 y 4 para el primer circulo: "))) # Solicita que vuelva a ingresar ya que se ah ingresado un dato incorrecto.

y = round(float(raw_input("\nIngrese el número del segundo circulo: "))) # El usuario ingresa el primer dato. Si se escribe un número con decimales, lo redondeará.
while (y<1 or y>4 or x==y):
  y = round(float(raw_input("Vuelva a ingresar un número entre 1 y 4 para el segundo circulo: "))) # Solicita que vuelva a ingresar ya que se ah ingresado un dato incorrecto.

# En caso que el usuario precione un caracter o una cadena de caracteres el programa mostrará un error y terminará su ejecución. No supimos como resolver ese problema.

if x==1 and y==2 or x==2 and y==1: # Casos en que el usuario ingrese 1 y 2.
  create_line(500, 725, 725, 500, "Black") # Crea la linea entre 1 y 2.
  centro_x = (500, 725)
  centro_y = (725, 500)
if x==2 and y==3 or x==3 and y==2: # Casos en que el usuario ingrese 2 y 3.
  create_line(725, 500, 500, 275, "Black") # Crea la linea entre 2 y 3.
  centro_x = (500, 275)
  centro_y = (725, 500)
if x==3 and y==4 or x==4 and y==3: # Casos en que el usuario ingrese 3 y 4.
  create_line(500, 275, 275, 500, "Black") # Crea la linea entre 3 y 4.
  centro_x = (275, 500)
  centro_y = (500, 275)
if x==4 and y==1 or x==1 and y==4: # Casos en que el usuario ingrese 1 y 4.
  create_line(275, 500, 500, 725, "Black") # Crea la linea entre 1 y 4.
  centro_x = (275, 500)
  centro_y = (500, 725)
if x==1 and y==3 or x==3 and y==1: # Casos en que el usuario ingrese 1 y 3.
  create_line(500, 725, 500, 275, "Black") # Crea la linea entre 1 y 3.
  centro_x = (500, 725)
  centro_y = (500, 275)
if x==2 and y==4 or x==4 and y==2: # Casos en que el usuario ingrese 2 y 4.
  create_line(725, 500, 275, 500, "Black") # Crea la linea entre 2 y 4.
  centro_x = (275, 500)
  centro_y = (725, 500)

# Ecuación de la recta resultante al unir los círculos seleccionados:

if centro_x[0] == centro_y[0]: 
  formula = "x = 500" # Ocurre cuando se genera una pendiente vertical.
else:
  pendiente = (centro_x[1] - centro_y[1]) / (centro_x[0] - centro_y[0]) # Ecuación de la pendiente.
  ordenada = centro_x[1] - pendiente * centro_x[0] # Ecuación de la ordenada.
  formula = "y = " + str(pendiente) + "x + " + str(ordenada) # Ecuación de la recta resultante final.

create_text(700, 50, formula, 5, "W") # Muestra la ecuación resultante en la pantalla gráfica.

print "\nUsted trazó la línea entre los circulos %d y %d." %(x, y) #Imprime en la ultima línea del programa entre que circulos se dibujó la recta.