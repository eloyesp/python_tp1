center_x = center_y = 500

def circulo(lado):
  x = center_x
  y = center_y
  radio = 100
  borde = 'Red'
  relleno = 'Blue'
  desplazamiento = 300
  if lado == "centro":
    radio = 200
  if lado == "arriba":
    y += desplazamiento
    relleno = "Yellow"
  if lado == "abajo":
    y -= desplazamiento
    relleno = "Yellow"
  if lado == "derecha":
    x += desplazamiento
    relleno = "Red"
  if lado == "izquierda":
    x -= desplazamiento
    relleno = "Green"
  create_filled_circle(x, y, radio, borde, relleno)

circulo("abajo")
circulo("arriba")
circulo("derecha")
circulo("izquierda")
circulo("centro")
